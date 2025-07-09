import os
import shutil

import allure_combine
from datetime import datetime
from framework.global_var import GlobalVar

def report_generator():
    """
    Output static allure report.
    """

    # Record the current time to differentiate folder names for different reports.
    GlobalVar.TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Add timestamp to file name
    GlobalVar.ALLURE_INDEX = GlobalVar.ALLURE_INDEX + GlobalVar.TIMESTAMP

    # Generate allure report
    generate_cmd = f'{GlobalVar.ALLURE} generate {GlobalVar.ALLURE_TMP} --clean -o {GlobalVar.ALLURE_INDEX}'
    print(f"執行命令： {generate_cmd}")
    try:
        ret = os.system(generate_cmd)
        if ret != 0:
            print("❌ Allure generate 執行失敗：命令返回非 0 狀態，請檢查命令或環境配置")
            return
        print(f'✅ Allure generate 執行成功，dir: {GlobalVar.ALLURE_INDEX}')
    except Exception as e:
        print(f'❌ Allure generate 執行異常：{e}')
        return


    # Combine allure report
    try:
        allure_combine.combine_allure(GlobalVar.ALLURE_INDEX)
        print(f'✅ 成功: 已生成 complete.html 於: {GlobalVar.ALLURE_INDEX}')
    except Exception as e:
        print(f'❌ 失敗: 未生成 complete.html 於: {GlobalVar.ALLURE_INDEX}\n{e}')


    # If there are more than 10 reports, delete the oldest ones
    all_items = os.listdir(GlobalVar.NEW_REPORT_PATH)

    report_folders = []
    for item in all_items:
        if item.startswith('allure-report_'):
            report_folders.append(item)

    report_folders.sort(reverse=True)  # Sort by timestamp (newest first)

    if len(report_folders) > 10:
        reports_to_delete = report_folders[10:]
        for folder in reports_to_delete:
            folder_path = os.path.join(GlobalVar.NEW_REPORT_PATH, folder)
            try:
                shutil.rmtree(folder_path)  # Delete the folder and its contents
                print(f'✅ 成功: 已刪除舊的報告資料夾：{folder_path}')
            except Exception as e:
                print(f'❌ 失敗: 無法刪除資料夾 {folder_path}：{e}')