import asyncio
import logging
import pytest
import argparse
import json
import sys
import os
from pathlib import Path
from typing import List, Tuple, Callable, Set
from concurrent.futures import ThreadPoolExecutor
from perl1_start_script import test_analyzer as analyzer_check
import sborka_sinhron as module1
import sborka_sinhron_blades as module2
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))
path= project_root / 'set_conf.json'
with open( path, 'r', encoding='utf-8') as f:
             data = json.load(f)
             setting = data['selected_file']
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(message)s',
    datefmt='%H:%M:%S',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger('WorkflowTest')

executor = ThreadPoolExecutor(max_workers=8)

class FunctionGroupTester:
    def __init__(self, selected_groups: Set[int] = None):
        self.function_pairs = [
            (module1.initialization, module2.initialization_blade, 1604),
            (module1.tab_scan, module2.tab_scan_blade, 1382),
            (module1.line_power_on, module2.line_power_on_blade, 1383),
            (module1.ALS_mode_change, module2.ALS_mode_change_blade, 1384),
            (module1.FEC_mode_EFEC, module2.FEC_mode_EFEC_blade, 1385),
            (module1.FEC_mode_G709, module2.FEC_mode_G709_blade, 1385),
            (module1.FEC_mode_off, module2.FEC_mode_off_blade, 1385),
            (module1.FEC_mode_G709_rep, module2.FEC_mode_G709_rep_blade, 1385),
            (module1.ALS_status_AutoImp, module2.ALS_status_ImpAuto_blade, 1386),
            (module1.ALS_status_ImpAuto, module2.ALS_status_AutoImp_blade, 1386),
            (module1.ALS_status_off, module2.ALS_status_off_blade, 1386),
            (module1.line_power_off, module2.line_power_off_blade, 1387),
            (module1.journal_check, module2.journal_check_blade, 1388),
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
        func1, func2, test_case_id = self.function_pairs[pair_idx]
        group_num = pair_idx + 1
        
        if self.selected_groups and group_num not in self.selected_groups:
            return {
                'group': group_num,
                'passed': True,
                'details': [],
                'skipped': True,
                'test_case_id': test_case_id
            }

        result = {
            'group': group_num,
            'passed': True,
            'details': [],
            'skipped': False,
            'test_case_id': test_case_id
        }

    
# Выполняем функции
        func1_success = await self._execute_single(func1)
        func2_success = await self._execute_single(func2)
        use_pytest = '--pytest' in sys.argv
        if not all([func1_success, func2_success]):
            result['passed'] = False
            result['details'].append("Ошибка выполнения функций")
            
        if group_num == 1 and not all([func1_success, func2_success]):
                    result['passed'] = False
                    result['details'].append(f"Проверьте подключение к сети")
                    if not args.no_kiwi: 
                        await self._update_kiwi_status(test_case_id=result['test_case_id'], passed=False, details=result['details'])
                    if use_pytest:
                        pytest.exit("Ошибка подключения к веб-интерфейсу")
                    else:
                        sys.exit()

# Проверка контрольной точки
        checkpoint_success = True
        if group_num in self.checkpoints:
            checkpoint_success = await self._check_checkpoint(group_num)
            if not checkpoint_success:
                result['passed'] = False
                result['details'].append(f"Ошибка проверки анализатора")
                if not args.no_kiwi:         
                    await self._update_kiwi_status(result['test_case_id'], result['passed'], result['details'])
        return result
        
    async def _execute_single(self, func: Callable) -> bool:
#Выполняет одну функцию
        try:
            if asyncio.iscoroutinefunction(func):
                result = await func()
            else:
                result = await self._run_sync_in_thread(func)
            
            if result is False:
                return False
            elif result is None:
                return False    
                
            return True
        except Exception as e:
            logger.error(f"Ошибка в {func.__name__}: {str(e)}")
            return False
        
    async def _check_checkpoint(self, group_num: int) -> bool:
        """Проверяет контрольную точку"""
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

    async def _update_kiwi_status(self, test_case_id: int, passed: bool, details: list):
#Обновление статуса в Kiwi
        try:
            from lib.UtilsManager import UtilsManager
            test_cfg = UtilsManager()
            
            config_path = Path(f'/home/kihafrichick/Документы/Автоматизация квазар/рабочий вариант/librarys/autotest_qaz/{setting}')
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
            
            if passed:
                status = 'PASSED'
                comment = "Все проверки пройдены успешно"
            else:
                status = 'FAILED'
                comment = f"{' | '.join(details)}"
            
            test_cfg.update_kiwi(config['test_run_id'], test_case_id, status, comment)
            #logger.info(f"Kiwi обновлен: TestCase {test_case_id} -> {status},{comment}")
            
        except Exception as e:
            logger.error(f"Ошибка при обновлении Kiwi: {str(e)}")

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

@pytest.fixture(scope="session")
def selected_groups():
    groups_str = os.environ.get('TEST_GROUPS', '')
    return parse_group_selection(groups_str)

@pytest.mark.asyncio
@pytest.mark.parametrize("group_idx", list(range(13)))
async def test_function_group(group_idx, selected_groups):
    """Тестирование группы функций"""
    tester = FunctionGroupTester(selected_groups)
    result = await tester.test_function_pair(group_idx)
    
    try:    
        if result.get('skipped', False):
            pytest.skip(f"Группа {result['group']} пропущена - не выбрана для запуска")

        if not result['passed']:
            pytest.fail()
    except SystemExit as e:
        if group_idx == 0:
           pytest.exit(f"Критическая ошибка в группе 0! Код выхода: {e.code}", returncode=1)                
if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--firefox',action='store_true')
    parser.add_argument('--groups')
    parser.add_argument('--pytest',action='store_true')
    parser.add_argument('--no-kiwi',action='store_true')
    parser.add_argument('--headless',action='store_true')
    
    args = parser.parse_args()
    # Основная логика выполняется только если не запрашивалась помощь
    selected_groups = parse_group_selection(args.groups) if args.groups else None
    if args.pytest:
        if args.groups:
            os.environ['TEST_GROUPS'] = args.groups
        # Запускаем pytest напрямую
        pytest_args = [__file__, '-v', '--tb=short']  # Добавляем короткий traceback
        exit_code = pytest.main(pytest_args)
        sys.exit(exit_code)
    else:
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
    try:  
        asyncio.run(run_selected_tests())
    except KeyboardInterrupt:  
        sys.exit(1)     