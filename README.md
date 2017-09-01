# Home Assistent Config Files

Home Assistnat config files.

## Alexa Integration

Integrate home assitant running on raspberry pi into Alexa custom skill, using some custom piece of python to access SkyQ

### Requirments

1. Home Assistant - https://home-assistant.io/
2. Alexa and developer account to create skill (please follow instruction on home assitant page)

### Known Issues

Sky Hub have no way of creating ARP table so Wake On Lan is not very reliable.
Probably becaouse after a while a temp ARP table is expired and magic packet cannot find MAC of TV.
Works on within after tv is turn on for a short period.
Workourn was to use a SkyQ and CEC to allow SkyQ turn on tv on wake up.

### Current Intents:

 1. TurnOnIntent
 2. TurnOffIntent
 3. MuteIntent
 4. UnMuteIntent
 5. VolumeUpIntent
 6. VolumeDownIntent
 7. PlayIntent
 8. PauseIntent
 
### Work in Progress
-sky q record
-tv set volume to x
- open netflix , amazon etc on tv
 
 
 ### Usage
 1. Alexa ask Bob to *[ turn on | power on | switch on ]* *[ skyq | tv ]*
 2. Alexa ask Bob to *[ turn off | power off | switch off ]* *[skyq | tv ]*
 3. Alexa ask Bob to *[ mute | silence ]* *[ tv ]*
 4. Alexa ask Bob to unmute *[ tv ]*
 5. Alexa ask Bob to *[ volume up | increase ]*  *[ tv ]*
 6. Alexa ask Bob to turn on *[skyq | tv ]*
 7. Alexa ask Bob to play *[skyq | tv ]*
 8. Alexa ask Bob to pause *[skyq | tv ]*

 
 
 
 
 
