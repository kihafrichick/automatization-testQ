import asyncio
import logging
import pytest
import argparse
from typing import List, Tuple, Callable, Set
from concurrent.futures import ThreadPoolExecutor
from perl_start_script import test_analyzer as analyzer_check
import sborka_sinhron as module1
import sborka_sinhron_blades as module2
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(message)s',
    datefmt='%H:%M:%S',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger('WorkflowTest')

executor = ThreadPoolExecutor(max_workers=4)

class FunctionGroupTester:
    def __init__(self, selected_groups: Set[int] = None):
        self.function_pairs = [
            (module1.initialization, module2.initialization_blade),
            (module1.tab_scan, module2.tab_scan_blade),
            (module1.line_power_on, module2.line_power_on_blade),
            (module1.ALS_mode_change, module2.ALS_mode_change_blade),
            (module1.FEC_mode_EFEC, module2.FEC_mode_EFEC_blade),
            (module1.FEC_mode_G709, module2.FEC_mode_G709_blade),
            (module1.FEC_mode_off, module2.FEC_mode_off_blade),
            (module1.FEC_mode_G709_rep, module2.FEC_mode_G709_rep_blade),
            (module1.ALS_status_AutoImp, module2.ALS_status_ImpAuto_blade),
            (module1.ALS_status_ImpAuto, module2.ALS_status_AutoImp_blade),
            (module1.ALS_status_off, module2.ALS_status_off_blade),
            (module1.line_power_off, module2.line_power_off_blade),
            (module1.journal_check, module2.journal_check_blade),
        ]
        self.checkpoints = {4, 5, 6, 7, 8, 9, 10, 11}
        self.checkpoint_timeout = 1.0 
        self.max_checkpoint_attempts = 3
        self.selected_groups = selected_groups
        
    async def _run_sync_in_thread(self, sync_func: Callable) -> bool:
        """Запускает синхронную функцию в отдельном потоке"""
        try:
            return await asyncio.get_event_loop().run_in_executor(
                executor,
                sync_func
            )
        except Exception as e:
            logger.error(f"Ошибка в синхронной функции: {str(e)}")
            return False

    async def test_function_pair(self, pair_idx: int) -> dict:
        """Тестирует одну группу функций"""
        func1, func2 = self.function_pairs[pair_idx]
        group_num = pair_idx + 1
        
        if self.selected_groups and group_num not in self.selected_groups:
            return {
                'group': group_num,
                'passed': True,
                'details': [],
                'skipped': True
            }

        result = {
            'group': group_num,
            'passed': True,
            'details': [],
            'skipped': False
        }

        # Выполняем функции
        func1_success = await self._execute_single(func1)
        func2_success = await self._execute_single(func2)
        
        if not all([func1_success, func2_success]):
            result['passed'] = False
            result['details'].append(f"Ошибка выполнения функций")

        # Проверка контрольной точки
        if group_num in self.checkpoints:
            checkpoint_result = await self._check_checkpoint(group_num)
            if not checkpoint_result:
                result['passed'] = False
                result['details'].append(f"Провалена контрольная точка")

        return result

    async def _execute_single(self, func: Callable) -> bool:
        """Выполняет одну функцию"""
        try:
            if asyncio.iscoroutinefunction(func):
                result = await func()
            else:
                result = await self._run_sync_in_thread(func)
            if result is False:
                logger.error(f"Функция {func.__name__} вернула False")
                return False
            elif result is None:
                logger.warning(f"Функция {func.__name__} вернула None")
                return False    
                
            return True
        except Exception as e:
            logger.error(f"Ошибка в {func.__name__}: {str(e)}")
            return False

    async def _check_checkpoint(self, group_num: int) -> bool:
        for attempt in range(self.max_checkpoint_attempts):
            try:
                result = await asyncio.wait_for(
                    self._run_sync_in_thread(analyzer_check),
                    timeout=self.checkpoint_timeout
                )
                if result:
                    return True
                logger.warning(f"Группа {group_num}: попытка {attempt+1} - ложный результат")
            except asyncio.TimeoutError:
                logger.warning(f"Группа {group_num}: таймаут попытки {attempt+1}")
            except Exception as e:
                logger.error(f"Группа {group_num}: ошибка в попытке {attempt+1}: {e}")
            
            if attempt < self.max_checkpoint_attempts - 1:
                await asyncio.sleep(1.0 * (attempt + 1))
        return False

def parse_group_selection(groups_str: str) -> Set[int]:
    """Парсит строку с номерами групп в множество чисел"""
    selected_groups = set()
    if not groups_str:
        return selected_groups
    
    for part in groups_str.split(','):
        part = part.strip()
        if '-' in part:
            start, end = map(int, part.split('-'))
            selected_groups.update(range(start, end + 1))
        else:
            selected_groups.add(int(part))
    
    return selected_groups

# Генерация тестов
def create_test_function(group_idx, selected_groups: Set[int]):
    @pytest.mark.asyncio
    async def test_implementation():
        tester = FunctionGroupTester(selected_groups)
        result = await tester.test_function_pair(group_idx)
        if result.get('skipped', False):
            pytest.skip(f"Группа {result['group']} пропущена - не выбрана для запуска")
        assert result['passed'], f"Группа {result['group']} провалена: {' | '.join(result['details'])}"
    
    test_implementation.__name__ = f"test_group_{group_idx+1}"
    return test_implementation

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Запуск тестовых групп функций')
    parser.add_argument('--groups', '-g', type=str, help='Номера групп для запуска (например: 1,3,5-8)')
    parser.add_argument('--pytest', action='store_true', help='Запустить через pytest')
    args = parser.parse_args()
    
    # Парсим выбранные группы
    selected_groups = parse_group_selection(args.groups) if args.groups else None

    if args.pytest:
        # Создаем и регистрируем тесты для pytest
        for idx in range(len(FunctionGroupTester().function_pairs)):
            globals()[f"test_group_{idx+1}"] = create_test_function(idx, selected_groups)
    else:
        # Прямой запуск
        async def run_selected_tests():
            tester = FunctionGroupTester(selected_groups)
            for idx in range(len(tester.function_pairs)):
                result = await tester.test_function_pair(idx)
                if result.get('skipped', False):
                    status = "SKIPPED"
                else:
                    status = "PASSED" if result['passed'] else "FAILED"
                print(f"Группа {result['group']}: {status}")
                if result['details']:
                    print("   Причина:", " | ".join(result['details']))
        
        asyncio.run(run_selected_tests())