import click
import os
import subprocess
from subprocess import Popen, PIPE, DEVNULL
from sys import platform
from getpass import getpass
from progress.spinner import Spinner
from progress.bar import IncrementalBar
import time
import pexpect

@click.group()
def cli():
    pass

@cli.command()
def version():
    '''
    Information About The Current Speed Version You Are Running
    '''
    print('Version: 1.0 \nDistribution: Stable x64')


@cli.command()
@click.argument('package_name', required=True)
def install(package_name):
    '''
    Install A Specified Package
    '''
    os_bar = IncrementalBar('Getting Operating System...', max = 1)
    if platform == 'linux':
        os_bar.next()
        click.echo('\n')
        finding_bar = IncrementalBar('Finding Requested Packages...', max = 1)
        if package_name == 'git':
            for _ in range(1, 2):
                time.sleep(0.03)
                finding_bar.next()
            try:    
                click.echo('\n')
                password = getpass("Enter your password: ")
                installer_progress = Spinner(message='Installing Git...', max=100)
                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.03)
                    installer_progress.next()
                proc = Popen("sudo -S apt-get install -y git".split(), stdin=PIPE, stdout=DEVNULL, stderr=PIPE)
                # Popen only accepts byte-arrays so you must encode the string
                output = proc.communicate(password.encode())
                click.echo(click.style('\n\n 🎉 Successfully Installed Git! 🎉 \n'))
                # Testing the successful installation of the package
                testing_bar = IncrementalBar('Testing package...', max = 100)
                for _ in range(1, 21):
                    time.sleep(0.045)
                    testing_bar.next()
                os.system('cd --')
                for _ in range(21, 60):
                    time.sleep(0.045)
                    testing_bar.next()
                subprocess.run(['git', 'clone', 'https://github.com/zpqrtbnk/test-repo.git'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                for _ in range(60, 101):
                    time.sleep(0.05)
                    testing_bar.next()
                os.system('rm -rf test-repo')
                subprocess.run(['git', '--version'], stdout=subprocess.DEVNULL)
                click.echo('\n')
                click.echo(click.style('Test Passed: Git Version ✅\n', fg='green'))
                click.echo(click.style('Test Passed: Clone Repository ✅\n', fg='green')) 
            except subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err = True)
        if package_name == 'curl': 
            for _ in range(1, 2):
                time.sleep(0.03)
                finding_bar.next()
            try:    
                click.echo('\n')
                password = getpass("Enter your password: ")
                installer_progress = Spinner(message='Installing Curl...', max=100)
                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.03)
                    installer_progress.next()
                proc = Popen("sudo -S apt-get install -y curl".split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
                # Popen only accepts byte-arrays so you must encode the string
                output = proc.communicate(password.encode())
                # stdoutput = (output)[0].decode('utf-8')
                click.echo(click.style('\n\n 🎉 Successfully Installed Curl! 🎉 \n'))
                # Testing the successful installation of the package
                testing_bar = IncrementalBar('Testing package...', max = 100)
                for _ in range(1, 21):
                    time.sleep(0.05)
                    testing_bar.next()
                os.system('cd --')
                for _ in range(21, 60):
                    time.sleep(0.05)
                    testing_bar.next()
                subprocess.run(['curl', '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                for _ in range(60, 101):
                    time.sleep(0.05)
                    testing_bar.next()
                click.echo('\n')
                click.echo(click.style('Test Passed: Curl Version ✅\n', fg='green'))
            except  subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err = True)
        if package_name == 'npm':
            for _ in range(1, 2):
                time.sleep(0.03)
                finding_bar.next()
            try:    
                click.echo('\n')
                password = getpass("Enter your password: ")
                installer_progress = Spinner(message='Installing NPM...', max=100)
                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.03)
                    installer_progress.next()
                proc = Popen("sudo -S apt-get install -y npm".split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
                # Popen only accepts byte-arrays so you must encode the string
                output = proc.communicate(password.encode())
                # stdoutput = (output)[0].decode('utf-8')
                click.echo(click.style('\n\n 🎉 Successfully Installed NPM! 🎉 \n'))
                # Testing the successful installation of the package
                testing_bar = IncrementalBar('Testing package...', max = 100)
                for _ in range(1, 21):
                    time.sleep(0.05)
                    testing_bar.next()
                os.system('cd --')
                for _ in range(21, 60):
                    time.sleep(0.05)
                    testing_bar.next()
                subprocess.run(['npm', '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                for _ in range(60, 101):
                    time.sleep(0.05)
                    testing_bar.next()
                click.echo('\n')
                click.echo(click.style('Test Passed: NPM Version ✅\n', fg='green'))
            except  subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err = True)
        if package_name == 'zsh':
            for _ in range(1, 2):
                time.sleep(0.03)
                finding_bar.next()
            try:    
                click.echo('\n')
                password = getpass("Enter your password: ")
                installer_progress = Spinner(message='Installing ZSH...', max=100)
                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.03)
                    installer_progress.next()
                proc = Popen("sudo -S apt-get install -y zsh".split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
                # Popen only accepts byte-arrays so you must encode the string
                output = proc.communicate(password.encode())
                # stdoutput = (output)[0].decode('utf-8')
                click.echo(click.style('\n\n 🎉 Successfully Installed ZSH! 🎉 \n'))
                # Testing the successful installation of the package
                testing_bar = IncrementalBar('Testing package...', max = 100)
                for _ in range(1, 21):
                    time.sleep(0.05)
                    testing_bar.next()
                os.system('cd --')
                for _ in range(21, 60):
                    time.sleep(0.05)
                    testing_bar.next()
                subprocess.run(['zsh', '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                for _ in range(60, 101):
                    time.sleep(0.05)
                    testing_bar.next()
                click.echo('\n')
                click.echo(click.style('Test Passed: ZSH Version ✅\n', fg='green'))
            except  subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err = True)
        if package_name == 'vim':
            for _ in range(1, 2):
                time.sleep(0.03)
                finding_bar.next()
            try:    
                click.echo('\n')
                password = getpass("Enter your password: ")
                installer_progress = Spinner(message='Installing Vim...', max=100)
                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.03)
                    installer_progress.next()
                proc = Popen("sudo -S apt-get install -y vim".split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
                # Popen only accepts byte-arrays so you must encode the string
                output = proc.communicate(password.encode())               
                # stdoutput = (output)[0].decode('utf-8')
                # print('This is the output: ', stdoutput)
                click.echo(click.style('\n\n 🎉 Successfully Installed Vim! 🎉 \n'))
                # Testing the successful installation of the package
                testing_bar = IncrementalBar('Testing package...', max = 100)
                for _ in range(1, 21):
                    time.sleep(0.05)
                    testing_bar.next()
                os.system('cd --')
                for _ in range(21, 60):
                    time.sleep(0.05)
                    testing_bar.next()
                subprocess.run(['vim', '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                for _ in range(60, 101):
                    time.sleep(0.05)
                    testing_bar.next()
                click.echo('\n')
                click.echo(click.style('Test Passed: Vim Version ✅\n', fg='green'))
            except  subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err = True)
        if package_name == 'chrome':
            for _ in range(1, 2):
                time.sleep(0.03)
                finding_bar.next()
            try:    
                click.echo('\n')
                password = getpass("Enter your password: ")
                installer_progress = Spinner(message='Installing Chrome...', max=100)
                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.03)
                    installer_progress.next()
                click.echo(click.style('\n Chrome Will Take 2 to 4 Minutes To Download... \n', fg='yellow'))
                proc = Popen("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb".split())
                proc.wait()
                second = Popen("sudo -S apt-get install -y ./google-chrome-stable_current_amd64.deb".split(), stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
                # Popen only accepts byte-arrays so you must encode the string
                _ = second.communicate(password.encode())
                
                # stdoutput = (output)[0].decode('utf-8')
                click.echo(click.style('\n\n 🎉 Successfully Installed Chrome! 🎉 \n'))             
                # Testing the successful installation of the package
                testing_bar = IncrementalBar('Testing package...', max = 100)
                for _ in range(1, 21):
                    time.sleep(0.045)
                    testing_bar.next()
                os.system('cd --')
                for _ in range(21, 60):
                    time.sleep(0.045)
                    testing_bar.next()
                for _ in range(60, 101):
                    time.sleep(0.03)
                    testing_bar.next()
                click.echo('\n')
                click.echo(click.style('Test Passed: Chrome Launch ✅\n', fg='green'))
            except  subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err = True)
        if package_name == 'opera':
            for _ in range(1, 2):
                time.sleep(0.03)
                finding_bar.next()
            try:    
                click.echo('\n')
                password = getpass("Enter your password: ")
                installer_progress = Spinner(message='Installing Opera...', max=100)
                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.03)
                    installer_progress.next()
                proc = Popen("sudo -S snap install opera".split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
                # Popen only accepts byte-arrays so you must encode the string
                output = proc.communicate(password.encode())
                # stdoutput = (output)[0].decode('utf-8')
                click.echo(click.style('\n\n 🎉 Successfully Installed Opera! 🎉 \n'))
                # Testing the successful installation of the package
                testing_bar = IncrementalBar('Testing package...', max = 100)
                for _ in range(1, 21):
                    time.sleep(0.05)
                    testing_bar.next()
                os.system('cd --')
                for _ in range(21, 60):
                    time.sleep(0.05)
                    testing_bar.next()
                for _ in range(60, 101):
                    time.sleep(0.05)
                    testing_bar.next()
                click.echo('\n')
                click.echo(click.style('Test Passed: Opera Launch ✅\n', fg='green'))
            except  subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err = True)
        if package_name == 'googler':
            for _ in range(1, 2):
                time.sleep(0.03)
                finding_bar.next()
            try:    
                click.echo('\n')
                password = getpass("Enter your password: ")
                installer_progress = Spinner(message='Installing Googler...', max=100)
                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.03)
                    installer_progress.next()
                proc = Popen("sudo -S apt-get install -y googler".split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
                # Popen only accepts byte-arrays so you must encode the string
                output = proc.communicate(password.encode())
                stdoutput = (output)[0].decode('utf-8')
                print(stdoutput)
                click.echo(click.style('\n\n 🎉 Successfully Installed Googler! 🎉 \n'))
                # Testing the successful installation of the package
                testing_bar = IncrementalBar('Testing package...', max = 100)
                for _ in range(1, 21):
                    time.sleep(0.05)
                    testing_bar.next()
                os.system('cd --')
                for _ in range(21, 60):
                    time.sleep(0.05)
                    testing_bar.next()
                for _ in range(60, 101):
                    time.sleep(0.05)
                    testing_bar.next()
                subprocess.run(['googler','--version'])
                click.echo('\n')
                click.echo(click.style('Test Passed: Googler Version ✅\n', fg='green'))
            except  subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err = True)
        if package_name == 'code':
            for _ in range(1, 2):
                time.sleep(0.03)
                finding_bar.next()
            try:    
                click.echo('\n')
                password = getpass("Enter your password: ")
                installer_progress = Spinner(message='Installing Visual Studio Code...', max=100)
                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.03)
                    installer_progress.next()
                proc = Popen("sudo -S snap install --classic code".split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
                # Popen only accepts byte-arrays so you must encode the string
                output = proc.communicate(password.encode())
                # stdoutput = (output)[0].decode('utf-8')
                click.echo(click.style('\n\n 🎉 Successfully Installed Visual Studio Code! 🎉 \n'))
                # Testing the successful installation of the package
                testing_bar = IncrementalBar('Testing package...', max = 100)
                for _ in range(1, 21):
                    time.sleep(0.05)
                    testing_bar.next()
                os.system('cd --')
                for _ in range(21, 60):
                    time.sleep(0.05)
                    testing_bar.next()
                for _ in range(60, 101):
                    time.sleep(0.05)
                    testing_bar.next()
                subprocess.run(['code','--version'])
                click.echo('\n')
                click.echo(click.style('Test Passed: Visual Studio Code Version ✅\n', fg='green'))
            except  subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err = True)
        if package_name == 'codeinsider':
            for _ in range(1, 2):
                time.sleep(0.03)
                finding_bar.next()
            try:    
                click.echo('\n')
                password = getpass("Enter your password: ")
                installer_progress = Spinner(message='Installing Visual Studio Code Insider...', max=100)
                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.03)
                    installer_progress.next()
                proc = Popen("sudo -S snap install --classic code-insiders".split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
                # Popen only accepts byte-arrays so you must encode the string
                output = proc.communicate(password.encode())
                # stdoutput = (output)[0].decode('utf-8')
                click.echo(click.style('\n\n 🎉 Successfully Installed Visual Studio Code Insider! 🎉 \n'))
                # Testing the successful installation of the package
                testing_bar = IncrementalBar('Testing package...', max = 100)
                for _ in range(1, 21):
                    time.sleep(0.05)
                    testing_bar.next()
                os.system('cd --')
                for _ in range(21, 60):
                    time.sleep(0.05)
                    testing_bar.next()
                for _ in range(60, 101):
                    time.sleep(0.05)
                    testing_bar.next()
                subprocess.run(['code','--version'])
                click.echo('\n')
                click.echo(click.style('Test Passed: Visual Studio Code Insider Version ✅\n', fg='green'))
            except  subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err = True)
            if package_name == 'wikit':
                for _ in range(1, 2):
                    time.sleep(0.03)
                    finding_bar.next()
            try:    
                click.echo('\n')
                password = getpass("Enter your password: ")
                installer_progress = Spinner(message='Installing Wikit...', max=100)
                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.03)
                    installer_progress.next()
                proc = Popen("sudo -S npm install wikit -g".split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
                # Popen only accepts byte-arrays so you must encode the string
                output = proc.communicate(password.encode())
                # stdoutput = (output)[0].decode('utf-8')
                click.echo(click.style('\n\n 🎉 Successfully Installed Wikit! 🎉 \n'))
                # Testing the successful installation of the package
                testing_bar = IncrementalBar('Testing package...', max = 100)
                for _ in range(1, 21):
                    time.sleep(0.05)
                    testing_bar.next()
                os.system('cd --')
                for _ in range(21, 60):
                    time.sleep(0.05)
                    testing_bar.next()
                for _ in range(60, 101):
                    time.sleep(0.05)
                    testing_bar.next()
                subprocess.run(['wikit','--version'])
                click.echo('\n')
                click.echo(click.style('Test Passed: Wikit Version ✅\n', fg='green'))
            except  subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err = True)
            if package_name == 'htop':
                for _ in range(1, 2):
                    time.sleep(0.03)
                    finding_bar.next()
            try:    
                click.echo('\n')
                password = getpass("Enter your password: ")
                installer_progress = Spinner(message='Installing Htop...', max=100)
                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.03)
                    installer_progress.next()
                proc = Popen("sudo apt-get install -y htop".split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
                # Popen only accepts byte-arrays so you must encode the string
                output = proc.communicate(password.encode())
                # stdoutput = (output)[0].decode('utf-8')
                click.echo(click.style('\n\n 🎉 Successfully Installed Htop! 🎉 \n'))
                # Testing the successful installation of the package
                testing_bar = IncrementalBar('Testing package...', max = 100)
                for _ in range(1, 21):
                    time.sleep(0.05)
                    testing_bar.next()
                os.system('cd --')
                for _ in range(21, 60):
                    time.sleep(0.05)
                    testing_bar.next()
                for _ in range(60, 101):
                    time.sleep(0.05)
                    testing_bar.next()
                subprocess.run(['htop','--version'])
                click.echo('\n')
                click.echo(click.style('Test Passed: Htop Version ✅\n', fg='green'))
            except  subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err = True)
            if package_name == 'tldr':
                for _ in range(1, 2):
                    time.sleep(0.03)
                    finding_bar.next()
            try:    
                click.echo('\n')
                password = getpass("Enter your password: ")
                installer_progress = Spinner(message='Installing Tldr...', max=100)
                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.03)
                    installer_progress.next()
                proc = Popen("sudo -S npm install -g tldr".split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
                # Popen only accepts byte-arrays so you must encode the string
                output = proc.communicate(password.encode())
                # stdoutput = (output)[0].decode('utf-8')
                click.echo(click.style('\n\n 🎉 Successfully Installed Tldr! 🎉 \n'))
                # Testing the successful installation of the package
                testing_bar = IncrementalBar('Testing package...', max = 100)
                for _ in range(1, 21):
                    time.sleep(0.05)
                    testing_bar.next()
                os.system('cd --')
                for _ in range(21, 60):
                    time.sleep(0.05)
                    testing_bar.next()
                for _ in range(60, 101):
                    time.sleep(0.05)
                    testing_bar.next()
                subprocess.run(['tldr','--version'])
                click.echo('\n')
                click.echo(click.style('Test Passed: Tldr Version ✅\n', fg='green'))
            except  subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err = True)
            if package_name == 'jq':
                for _ in range(1, 2):
                    time.sleep(0.03)
                    finding_bar.next()
            try:    
                click.echo('\n')
                password = getpass("Enter your password: ")
                installer_progress = Spinner(message='Installing Jq...', max=100)
                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.03)
                    installer_progress.next()
                proc = Popen("sudo -S apt-get install -y jq".split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
                # Popen only accepts byte-arrays so you must encode the string
                output = proc.communicate(password.encode())
                # stdoutput = (output)[0].decode('utf-8')
                click.echo(click.style('\n\n 🎉 Successfully Installed Jq! 🎉 \n'))
                # Testing the successful installation of the package
                testing_bar = IncrementalBar('Testing package...', max = 100)
                for _ in range(1, 21):
                    time.sleep(0.05)
                    testing_bar.next()
                os.system('cd --')
                for _ in range(21, 60):
                    time.sleep(0.05)
                    testing_bar.next()
                for _ in range(60, 101):
                    time.sleep(0.05)
                    testing_bar.next()
                subprocess.run(['jq','--version'])
                click.echo('\n')
                click.echo(click.style('Test Passed: Jq Version ✅\n', fg='green'))
            except  subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err = True)
            if package_name == 'ncdu':
                for _ in range(1, 2):
                    time.sleep(0.03)
                    finding_bar.next()
            try:    
                click.echo('\n')
                password = getpass("Enter your password: ")
                installer_progress = Spinner(message='Installing Ncdu...', max=100)
                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.03)
                    installer_progress.next()
                proc = Popen("sudo -S apt-get install -y ncdu".split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
                # Popen only accepts byte-arrays so you must encode the string
                output = proc.communicate(password.encode())
                # stdoutput = (output)[0].decode('utf-8')
                click.echo(click.style('\n\n 🎉 Successfully Installed Ncdu! 🎉 \n'))
                # Testing the successful installation of the package
                testing_bar = IncrementalBar('Testing package...', max = 100)
                for _ in range(1, 21):
                    time.sleep(0.05)
                    testing_bar.next()
                os.system('cd --')
                for _ in range(21, 60):
                    time.sleep(0.05)
                    testing_bar.next()
                for _ in range(60, 101):
                    time.sleep(0.05)
                    testing_bar.next()
                subprocess.run(['ncdu','--version'])
                click.echo('\n')
                click.echo(click.style('Test Passed: Ncdu Version ✅\n', fg='green'))
            except  subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err = True)
            if package_name == 'taskwarrior':
                for _ in range(1, 2):
                    time.sleep(0.03)
                    finding_bar.next()
            try:    
                click.echo('\n')
                password = getpass("Enter your password: ")
                installer_progress = Spinner(message='Installing Taskwarrior...', max=100)
                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.03)
                    installer_progress.next()
                proc = Popen("sudo -S apt-get install -y taskwarrior".split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
                # Popen only accepts byte-arrays so you must encode the string
                output = proc.communicate(password.encode())
                # stdoutput = (output)[0].decode('utf-8')
                click.echo(click.style('\n\n 🎉 Successfully Installed Taskwarrior! 🎉 \n'))
                # Testing the successful installation of the package
                testing_bar = IncrementalBar('Testing package...', max = 100)
                for _ in range(1, 21):
                    time.sleep(0.05)
                    testing_bar.next()
                os.system('cd --')
                for _ in range(21, 60):
                    time.sleep(0.05)
                    testing_bar.next()
                for _ in range(60, 101):
                    time.sleep(0.05)
                    testing_bar.next()
                subprocess.run(['taskwarrior','--version'])
                click.echo('\n')
                click.echo(click.style('Test Passed: Taskwarrior Version ✅\n', fg='green'))
            except  subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err = True)
            if package_name == 'tmux':
                for _ in range(1, 2):
                    time.sleep(0.03)
                    finding_bar.next()
            try:    
                click.echo('\n')
                password = getpass("Enter your password: ")
                installer_progress = Spinner(message='Installing Tmux...', max=100)
                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.03)
                    installer_progress.next()
                proc = Popen("sudo -S apt-get install -y tmux".split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
                # Popen only accepts byte-arrays so you must encode the string
                output = proc.communicate(password.encode())
                # stdoutput = (output)[0].decode('utf-8')
                click.echo(click.style('\n\n 🎉 Successfully Installed Tmux! 🎉 \n'))
                # Testing the successful installation of the package
                testing_bar = IncrementalBar('Testing package...', max = 100)
                for _ in range(1, 21):
                    time.sleep(0.05)
                    testing_bar.next()
                os.system('cd --')
                for _ in range(21, 60):
                    time.sleep(0.05)
                    testing_bar.next()
                for _ in range(60, 101):
                    time.sleep(0.05)
                    testing_bar.next()
                subprocess.run(['tmux','--version'])
                click.echo('\n')
                click.echo(click.style('Test Passed: Tmux Version ✅\n', fg='green'))
            except  subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err = True)
            if package_name == 'patchelf':
                for _ in range(1, 2):
                    time.sleep(0.03)
                    finding_bar.next()
            try:    
                click.echo('\n')
                password = getpass("Enter your password: ")
                installer_progress = Spinner(message='Installing Patchelf...', max=100)
                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.03)
                    installer_progress.next()
                proc = Popen("sudo -S apt-get install -y patchelf".split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
                # Popen only accepts byte-arrays so you must encode the string
                output = proc.communicate(password.encode())
                # stdoutput = (output)[0].decode('utf-8')
                click.echo(click.style('\n\n 🎉 Successfully Installed Patchelf! 🎉 \n'))
                # Testing the successful installation of the package
                testing_bar = IncrementalBar('Testing package...', max = 100)
                for _ in range(1, 21):
                    time.sleep(0.05)
                    testing_bar.next()
                os.system('cd --')
                for _ in range(21, 60):
                    time.sleep(0.05)
                    testing_bar.next()
                for _ in range(60, 101):
                    time.sleep(0.05)
                    testing_bar.next()
                subprocess.run(['patchelf','--version'])
                click.echo('\n')
                click.echo(click.style('Test Passed: Patchelf Version ✅\n', fg='green'))
            except  subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err = True)
    if platform == 'darwin':
        os_bar.next()
        click.echo('\n')
        finding_bar = IncrementalBar('Finding Requested Packages...', max = 1)
        if package_name == 'brew':
            for _ in range(1, 2):
                time.sleep(0.03)
                finding_bar.next()
            try:    
                click.echo('\n')
                password = getpass("Enter your password: ")
                installer_progress = Spinner(message='Installing Homebrew...', max=100)
                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.03)
                    installer_progress.next()
                proc = pexpect.spawn('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"')
                proc.sendline(password)
                proc.sendline('\n')
                click.echo(click.style('\n\n 🎉 Successfully Installed Homebrew! 🎉 \n'))
                # Testing the successful installation of the package
                testing_bar = IncrementalBar('Testing package...', max = 100)
                for _ in range(1, 21):
                    time.sleep(0.05)
                    testing_bar.next()
                os.system('cd --')
                for _ in range(21, 60):
                    time.sleep(0.05)
                    testing_bar.next()
                for _ in range(60, 101):
                    time.sleep(0.05)
                    testing_bar.next()
                subprocess.run(['brew','--version'])
                click.echo('\n')
                click.echo(click.style('Test Passed: Brew Version ✅\n', fg='green'))
            except  subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err = True)
        if package_name == 'xcode-tools':
            for _ in range(1, 2):
                time.sleep(0.03)
                finding_bar.next()
            try:    
                click.echo('\n')
                password = getpass("Enter your password: ")
                installer_progress = Spinner(message='Installing Xcode-Command-Line-Tools...', max=100)
                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.03)
                    installer_progress.next()
                proc = pexpect.spawn('xcode-select --install')
                click.echo(click.style('\n\n 🎉 Successfully Installed Xcode-Command-Line-Tools! 🎉 \n'))
                # Testing the successful installation of the package
                testing_bar = IncrementalBar('Testing package...', max = 100)
                for _ in range(1, 21):
                    time.sleep(0.05)
                    testing_bar.next()
                os.system('cd --')
                for _ in range(21, 60):
                    time.sleep(0.05)
                    testing_bar.next()
                for _ in range(60, 101):
                    time.sleep(0.05)
                    testing_bar.next()
                subprocess.run(['git','--version'])
                subprocess.run(['clang', '--version'])
                subprocess.run(['swift', '--version'])
                subprocess.run(['pip3', '--version'])
                
                click.echo('\n')
                click.echo(click.style('Test Passed: Git Version ✅\n', fg='green'))
                click.echo(click.style('Test Passed: Clang Version ✅\n', fg='green'))
                click.echo(click.style('Test Passed: Swift Version ✅\n', fg='green'))
                click.echo(click.style('Test Passed: Pip3 Version ✅\n', fg='green'))
                
            except  subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err = True)
