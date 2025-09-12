import asyncio
import logging
import pytest
from typing import List, Tuple, Callable
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
    def __init__(self):
        self.function_pairs = [
            (module1.function_1, module2.function_14),
            (module1.function_2, module2.function_15),
            (module1.function_3, module2.function_16),
            (module1.function_4, module2.function_17),
            (module1.function_5, module2.function_18),
            (module1.function_6, module2.function_19),
            (module1.function_7, module2.function_20),
            (module1.function_8, module2.function_21),
            (module1.function_9, module2.function_22),
            (module1.function_10, module2.function_23),
            (module1.function_11, module2.function_24),
            (module1.function_12, module2.function_25),
            (module1.function_13, module2.function_26),
        ]
        self.checkpoints = { 4, 5, 6, 7, 8, 9, 10, 11}
        self.checkpoint_timeout = 1.0 
        self.max_checkpoint_attempts = 3
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
        result = {
            'group': group_num,
            'passed': True,
            'details': []
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

# Генерация тестов
def create_test_function(group_idx):
    @pytest.mark.asyncio
    async def test_implementation():
        tester = FunctionGroupTester()
        result = await tester.test_function_pair(group_idx)
        assert result['passed'], f"Группа {result['group']} провалена: {' | '.join(result['details'])}"
    
    test_implementation.__name__ = f"test_group_{group_idx+1}"
    return test_implementation

# Создаем и регистрируем тесты
for idx in range(len(FunctionGroupTester().function_pairs)):
    globals()[f"test_group_{idx+1}"] = create_test_function(idx)

if __name__ == "__main__":
    async def run_all_tests():
        tester = FunctionGroupTester()
        for idx in range(len(tester.function_pairs)):
            result = await tester.test_function_pair(idx)
            status = "PASSED" if result['passed'] else "FAILED"
            print(f"Группа {result['group']}: {status}")
            if result['details']:
                print("   Причина:", " | ".join(result['details']))
    
    asyncio.run(run_all_tests())