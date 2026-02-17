#This function will contain a list of buzz words people will use to try and override an AI agent

def security_check():
    #List of common prompt injections
    injections = ["ignore", "override", "bypass", "disable", "hypothetically", "pretend"]
    return injections
alerts = [] #wil store any alerts that are triggered

print('----Starting Security Check for Prompt Injections----\n')

try: 
    with open('logs.txt', 'r') as logs:
        content = logs.read().lower() #Reads the logs file and converts it to lowercase for easier comparison
        for word in security_check():
            if word in content:
                print(f'Alert: Potential Prompt Injection in progress! Detected word: {word}')
                alerts.append(word) #Adds the detected word to the alerts list
            

    with open('alerts.txt','w') as alert_file: #Opens a separate file to log any detected prompt injections for review
        for alert in alerts:
            alert_file.write(f'--Flagged injection word: {alert}.  Review the prompt sent!\n') #Writes any detected alerts to a separate file for review
        print("Alert log has been updated with detected prompt injections.")    
                 

except FileNotFoundError:
    print("No potential prompt injections detected.")

print('----Security Check Complete----')
print('Check alerts.txt for results of the security check.\n') 


