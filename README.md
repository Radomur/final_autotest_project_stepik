# final_autotest_project_stepik
comands run tests:
  pytest -v --tb=line --language=en test_main_page.py
  pytest -s --language=en test_product_page.py
  pytest -s -m "new" test_main_page.py
