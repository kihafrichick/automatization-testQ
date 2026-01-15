from work_funcs.import_file import *
from work_funcs.parse_funcs import*
from work_funcs.FuncTest_class import FunctionGroupTester

logger = logging.getLogger('WorkflowTest') 
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))
path= project_root / 'set_conf.json'
with open( path, 'r', encoding='utf-8') as f:
             data = json.load(f)
             setting = data["sborka_sinhron"]["conf_file"]
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(message)s',
    datefmt='%H:%M:%S',
    handlers=[logging.StreamHandler()]
)


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
        status_str = "PASSED" if result['passed'] else "FAILED"
        logger.info(f"Группа {result['group']} ({result['test_case_id']}): {status_str}")
        if result.get('details'):
            logger.info(f"   Детали: {' | '.join(result['details'])}")    
        if result.get('skipped', False):
            pytest.skip(f"Группа {result['group']} пропущена - не выбрана для запуска")

        if not result['passed']:
            # Передаем подробности в pytest, чтобы они были видны в отчете
            details_msg = " | ".join(result.get('details', [])) or f"Группа {result['group']} завершилась с ошибкой"
            pytest.fail(details_msg)
    except SystemExit as e:
        if group_idx == 0:
           pytest.exit(f"Критическая ошибка в группе 0! Код выхода: {e.code}", returncode=1)                
if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--firefox',action='store_true')
    parser.add_argument('--groups')
    parser.add_argument('--pytest',action='store_true')
    parser.add_argument('--nokiwi',action='store_true')
    parser.add_argument('--headless',action='store_true')
    
    args = parser.parse_args()
    # Основная логика выполняется только если не запрашивалась помощь
    selected_groups = parse_group_selection(args.groups) if args.groups else None
    if args.pytest:
        if args.groups:
            os.environ['TEST_GROUPS'] = args.groups
        # Запускаем pytest напрямую
        pytest_args = [__file__, '-v', '--tb=short', '-s']  # Добавляем короткий traceback и отключаем захват вывода
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