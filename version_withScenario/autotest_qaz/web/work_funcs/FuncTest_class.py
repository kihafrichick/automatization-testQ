from .import_file import *
import sborka_sinhron as module1
import sborka_sinhron_blades as module2
from perl1_start_script import test_analyzer as analyzer_check
logger = logging.getLogger('WorkflowTest')
executor = ThreadPoolExecutor(max_workers=6)
from  lib.UtilsManager import *

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
        self.all_execution_logs= []
        self.group_logs = {}
        
        
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
        self.all_execution_logs = []

        # Обработка выбора групп: пропущенные группы не выполняются и не отчитываются в Kiwi
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
        task1 = self._execute_single(func1)
        task2 = self._execute_single(func2)
        func1_success, func2_success = await asyncio.gather(task1, task2)

        use_pytest = '--pytest' in sys.argv

        if not all([func1_success, func2_success]):
            result['passed'] = False
            if self.all_execution_logs:
                result['details'].extend(self.all_execution_logs)
            else:
                # Если логи пусты, но функции вернули False, добавляем общее сообщение
                result['details'].append("Одна или обе функции группы завершились с ошибкой")

        if group_num == 1 and not all([func1_success, func2_success]):
            if '--nokiwi' not in sys.argv:
                await self.update_kiwi_status(
                    test_case_id=result['test_case_id'],
                    passed=result['passed'],
                    details=result['details'],
                )
            if use_pytest:
                pytest.exit("Ошибка подключения к веб-интерфейсу")
            else:
                sys.exit('Ошибка подключения к веб-интерфейсу')

        # Проверка контрольной точки
        checkpoint_success = True
        if group_num in self.checkpoints:
            checkpoint_success = await self._check_checkpoint(group_num)
            if not checkpoint_success:
                result['passed'] = False
                result['details'].append("Ошибка проверки анализатора")
                # Выводим человеко‑читаемое описание причин
                print(" | ".join(result['details']))

        # Обновляем Kiwi уже по итоговому статусу группы (включая контрольные точки)
        if '--nokiwi' not in sys.argv:
            await self.update_kiwi_status(
                test_case_id=result['test_case_id'],
                passed=result['passed'],
                details=result['details'],
            )

        return result
        
        
        
    async def _execute_single(self, func: Callable) -> bool:
        """
        Выполняет одну функцию и перехватывает её вывод.
        ВАЖНО: stdout всегда перехватывается, чтобы собирать логи для Kiwi,
        но в обычном режиме вывод сразу дублируется в консоль для наглядности.
        """

        try:
            # Просто выполняем функцию без перехвата
            if asyncio.iscoroutinefunction(func):
                result = await func()
            else:
                result = await self._run_sync_in_thread(func)
            
            # Логируем успех явно
            if result:
                logger.info(f" {func.__name__} успешно завершена")
            return bool(result)
        
        except Exception as e:
            logger.error(f" Ошибка в {func.__name__}: {str(e)}")
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

        
    async def update_kiwi_status(self, test_case_id: int, passed: bool, details: list):
#Обновление статуса в Kiwi
        try:
            from lib.UtilsManager import UtilsManager
            test_cfg = UtilsManager()
            config = test_cfg.load_config()
            status = 'PASSED' if passed else 'FAILED'
            comment = " | ".join(details) if details else ("Все проверки пройдены" if passed else "Ошибка выполнения")
            
            test_cfg.update_kiwi(config['test_run_id'], test_case_id, status, comment)
            #logger.info(f"KiwiTCMS обновлен: TestCase {test_case_id} -> {status}")
        
        except Exception as e:
            logger.error(f"ыОшибка обновления KiwiTCMS: {str(e)}")
