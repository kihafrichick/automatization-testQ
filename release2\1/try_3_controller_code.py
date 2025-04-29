import asyncio
import logging
import pytest
from typing import List, Tuple, Callable

# Настройка логгера
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(message)s',
    datefmt='%H:%M:%S',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger('WorkflowTest')

# Реальные импорты
from perl_start_script import test_analyzer as analyzer_check
import sborka_sinhron as module1
import sborka_sinhron_blades as module2

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
                await func()
            else:
                func()
            return True
        except Exception as e:
            logger.error(f"Ошибка в {func.__name__}: {str(e)}")
            return False

    async def _check_checkpoint(self, group_num: int) -> bool:
        """Проверяет контрольную точку"""
        try:
            return analyzer_check()
        except Exception as e:
            logger.error(f"Ошибка проверки точки {group_num}: {str(e)}")
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