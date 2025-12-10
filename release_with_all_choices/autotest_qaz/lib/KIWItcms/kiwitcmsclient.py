from tcms_api import TCMS
from datetime import datetime
import time
import os
import base64
import ssl
import logging
from typing import Optional
from typing import Dict, List, Optional, Union

class KiwiTCMSClient:
    """Класс для работы с Kiwi TCMS версии 14 через XML-RPC API"""
    
    def __init__(self):
        try:
            _create_unverified_https_context = ssl._create_unverified_context
        except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
                pass
        else:
    # Handle target environment that doesn't support HTTPS verification
            ssl._create_default_https_context = _create_unverified_https_context
        self.kiwi = TCMS().exec
        self.logger = logging.getLogger('KiwiTCMSClient')
        self._status_cache = None
        self.map_status=self.get_status_mappings()

    # region TestExecution Methods
    def get_execution(self, execution_id: int) -> Optional[Dict]:
        """Получить информацию о выполнении теста"""
        try:
            return self.kiwi.TestExecution.history(execution_id)
        except Exception as e:
            self.logger.error(f"Error getting execution {execution_id}: {str(e)}")
            return None
    
    def get_state_id(self,name:str):
        return self.map_status['name_to_id'][name]
    
    def add_comment_execution(self, execution_id: int,comment: str, **kwargs):
        try:
            result = self.kiwi.TestExecution.add_comment(execution_id,comment)
            return result
        except Exception as e:
            self.logger.error(f"Error updating execution {execution_id}: {str(e)}")
            return False   
         
    def update_execution(self, execution_id: int, status: Optional[int] = None,
                       comment: Optional[str] = None, **kwargs) -> bool:
        """
        Обновить выполнение теста
        
        :param execution_id: ID выполнения
        :param status: Новый статус
        :param comment: Новый комментарий
        :param kwargs: Дополнительные поля для обновления
        :return: True при успешном обновлении
        """
        
        try:
            updates = {}
            
           #status_id=self.get_state_id[status]
            if status:
                updates['status'] = status#self.validate_status(status)
            if comment:
                updates['comment'] = comment
                
            updates.update(kwargs)
            
            if not updates:
                self.logger.warning("No updates provided")
                return False
                
            result = self.kiwi.TestExecution.update(execution_id, updates)
            if comment:
                result = self.kiwi.TestExecution.add_comment(execution_id, updates['comment'])
            #self.logger.info(f"Updated execution {execution_id}: {updates}")
            return bool(result)
            
        except Exception as e:
            self.logger.error(f"Error updating execution {execution_id}: {str(e)}")
            return False
    
    def get_executions_for_run(self, run_id: int) -> List[Dict]:
        """Получить все выполнения для тестового прогона"""
        try:
            return self.kiwi.TestExecution.filter({'run_id': run_id})
        except Exception as e:
            self.logger.error(f"Error getting executions for run {run_id}: {str(e)}")
            return []
    # endregion
    
    # region TestExecutionStatus Methods
    def get_statuses(self, refresh_cache: bool = False) -> Dict[str, int]:
        """Получить словарь статусов {name: id}"""
        if self._status_cache and not refresh_cache:
            return self._status_cache
            
        try:
            statuses = self.kiwi.TestExecutionStatus.filter({})
            self._status_cache = {s['name']: s['id'] for s in statuses}
            return self._status_cache
        except Exception as e:
            self.logger.error(f"Error getting statuses: {str(e)}")
            return {}
    
    def validate_status(self, status: Union[str, int]) -> str:
        """
        Проверить и нормализовать статус выполнения
        
        :param status: Имя или ID статуса
        :return: Нормализованное имя статуса
        :raises ValueError: Если статус недопустим
        """
        statuses = self.get_statuses()
       # 

        if isinstance(status, int):
            for name, id_ in statuses.items():
                if id_ == status:
                    return name
            raise ValueError(f"Invalid status ID: {status}")
            
        status_upper = status.upper()
        if status_upper in statuses:
            return status_upper
            
        raise ValueError(f"Invalid status name: {status}. Valid statuses: {', '.join(statuses.keys())}")
    def get_status_mappings(self):
    
        statuses = self.kiwi.TestExecutionStatus.filter({})

      #  reverse_status_dict = {v: k for k, v in status_dict.items()}
        id_to_name = {s['id']: s['name'] for s in statuses}
        name_to_id = {s['name']: s['id'] for s in statuses}
     #    id_to_label = {s['id']: s['label'] for s in statuses}
    
        return {
        'id_to_name': id_to_name,
        'name_to_id': name_to_id,
        }
    # endregion
    
    # region TestRun Methods
    def get_test_run(self, run_id: int) -> Optional[Dict]:
        """Получить информацию о тестовом прогоне"""
        try:
            return self.kiwi.TestRun.get_cases(run_id)
        except Exception as e:
            self.logger.error(f"Error getting run {run_id}: {str(e)}")
            return None
    
    def create_test_run(self, plan_id: int, name: str, build_id: int,
                      manager_id: int, **kwargs) -> Optional[int]:
        """
        Создать новый тестовый прогон
        
        :param plan_id: ID тестового плана
        :param name: Название прогона
        :param build_id: ID сборки
        :param manager_id: ID менеджера
        :param kwargs: Дополнительные параметры
        :return: ID созданного прогона или None
        """
        try:
            params = {
                'plan': plan_id,
                'name': "Aвтоматический тест план",
                'summary': 'Run_'+ datetime.now().strftime("%Y%m%d"),  # Обязательно!
                'build': build_id,
                'manager': manager_id
            }
            params.update(kwargs)
            
            run_id = self.kiwi.TestRun.create(params)
            self.logger.info(f"Created test run {run_id}")
            return run_id
        except Exception as e:
            self.logger.error(f"Error creating test run: {str(e)}")
            return None
    def test_run_start(self, run_id):
        self.kiwi.TestRun.update(run_id, {
        'start_date': datetime.now(),  # Sets status to "Running"
        #'is_active': True
        })
        return
    def test_run_stop(self, run_id):
        self.kiwi.TestRun.update(run_id, {
        'stop_date': datetime.now(),  # Sets status to "Finished"
        #'is_active': False
        })
        return
    # endregion
    
    # region TestCase Methods
    
    def find_test_cases(self, **filters) -> List[Dict]:
        """Найти тест-кейсы по фильтрам"""
        try:
            return self.kiwi.TestCase.filter(filters)
        except Exception as e:
            self.logger.error(f"Error finding test cases: {str(e)}")
            return []
    # endregion
    
    def add_attachment_to_execution(self, run_id: int, filename: str, b64content: Optional[str] = None) -> bool:
        """
        Добавить вложение к выполнению теста
        
        :param case_id: ID выполнения
        :param filename: Путь к файлу
        :return: True при успешном добавлении
        """
        try:
            with open(filename, 'rb') as file:
                file_content = file.read()
                b64content = base64.b64encode(file_content).decode('ascii')
            filename = os.path.basename(filename)
            self.kiwi.TestRun.add_attachment(run_id, filename, b64content)
            self.logger.info(f"Added attachment '{filename}' to test case {run_id}")
            return True
        except Exception as e:
            self.logger.error(f"Error adding attachment to test case {run_id}: {str(e)}")
            return False
        

        # region User Methods
    def get_id_user(self,username:str):
        """
        Поиск id пользователя
        :return: id пользователя         
        """
        try:
            users = self.kiwi.User.filter({"username": username})
            return users[0]['id'] if users else None
        except Exception as e:
            self.logger.error(f"Error finding users: {str(e)}")
            
            return []
        
    
        # region Builds Methods
    def get_latest_build(self,product_id):
        """
        Поиск cборок
        :return: звращает последнюю сборку       
        """
        try:
            versions =self.kiwi.Version.filter({"product": product_id})
            if not versions:
                return []
    
            # Собираем ID версий
            version_ids = [v['id'] for v in versions]   
            # Получаем сборки для этих версий
            builds=self.kiwi.Build.filter({"version__in": version_ids})
            if not builds:
                return None
            latest_build = sorted(builds, key=lambda x: x['id'], reverse=True)[0]
            return latest_build
        except Exception as e:
            self.logger.error(f"Error finding users: {str(e)}")
           
            return []


    # region Common Methods
    def create_full_test_run(self,username:str,plan_id,product_id,name):
        """
        Creare full test run with test cases
        :return:       
        """
        id = self.get_id_user(str(username))
        build_id=self.get_latest_build(product_id)
        #print(f"ID: {build_id['id']}")#, Название: {build['name']}, Версия: {build['version']}")
        run=self.create_test_run(plan_id,name,build_id['id'],id)
        run_id=run['id']
        lentestcase=self.add_plan_cases_to_run(plan_id,run_id)
        return lentestcase, run_id

    def add_plan_cases_to_run(self,plan_id, run_id):    
        try:
     # Проверяем существование плана
            if not self.kiwi.TestPlan.filter({'id': plan_id}):
                raise ValueError(f"Тест-план ID {plan_id} не найден")
        
        # Получаем все тест-кейсы из плана
            test_cases = self.kiwi.TestCase.filter({"plan": plan_id})
        
            if not test_cases:
                return
        
            # Получаем кейсы, уже находящиеся в прогоне (для исключения дубликатов)
            existing_cases = {case['case'] for case in self.kiwi.TestRun.get_cases(run_id)}
        
            # Добавляем кейсы в прогон
            added_count = 0
            for i, case in enumerate(test_cases):
                case_id = case['id']
            
            # Пропускаем кейсы, уже добавленные в прогон
                if case_id in existing_cases:
                    continue
                
                try:
                    self.kiwi.TestRun.add_case(run_id, case_id)
                    added_count += 1               
                # Пауза для снижения нагрузки на сервер
                    if (i+1) % 20 == 0:
                        time.sleep(1)
                    
                except Exception as e:
                 print(f"Ошибка при добавлении кейса {case_id}: {str(e)}")
                 return None
        except Exception as e:
            print(f"Критическая ошибка: {str(e)}")
            return None
        return added_count