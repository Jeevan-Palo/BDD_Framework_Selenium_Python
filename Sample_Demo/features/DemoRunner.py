import sys
from behave import __main__ as Demo_runner
import shutil
import unittest
import glob

from json2html import *
import HTMLTestRunner
import unittest


if __name__ == '__main__':
    sys.stdout.flush()
    reporting_folder_name = 'report_folder_json_html'
    shutil.rmtree(reporting_folder_name, ignore_errors=True)
    # allure reporting related command line arguments
    reportingRelated = ' -f allure_behave.formatter:AllureFormatter -o ' + reporting_folder_name + '  '

    featureFilePath = ' feature_files/Demo1.feature '
    commonRunnerOptions = ' --no-capture --no-capture-stderr -f plain '
    fullRunnerOptions = featureFilePath + reportingRelated + commonRunnerOptions
    Demo_runner.main(fullRunnerOptions)

    # read resultant json file
    listOfJson = glob.glob(reporting_folder_name + "/*.json")
    finalJson = ''
    for cnt in range(0, len(listOfJson)):
        listOfJson[cnt] = ' {"' + "Scenario_" + str(cnt) + '"' + ' : ' + open(listOfJson[cnt], 'r').read() + '}'
        if cnt < (-1 + len(listOfJson)):
            listOfJson[cnt] = listOfJson[cnt] + ','
        finalJson = finalJson + listOfJson[cnt]
    finalJson = '[ ' + finalJson + ' ]'
    #
    # convert json to html using simple utility and publish report
    html_content = json2html.convert(json=finalJson)
    html_report_file = open(reporting_folder_name + '/' + 'index.html', 'w')
    html_report_file.write(html_content)
    html_report_file.close()
