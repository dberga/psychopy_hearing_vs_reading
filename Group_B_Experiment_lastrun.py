#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.81.00), noviembre 26, 2014, at 21:42
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'untitled'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\dber\\Desktop\\Final_Experiment_PsychoPy-2014-11-26\\Final Experiment PsychoPy\\Group_B_Experiment.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1366, 768), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "Start"
StartClock = core.Clock()
Start_Display = visual.TextStim(win=win, ori=0, name='Start_Display',
    text=u'Hola. Gracias por participar en nuestro experimento.\n\nPor favor, escucha el siguiente audio cuidadosamente. Por favor, usa los auriculares para esta tarea.\n\nAprieta cualquier boton para continuar.',    font=u'Arial',
    units='pix', pos=[0, 0], height=50, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "Audio_Display"
Audio_DisplayClock = core.Clock()
sound_1 = sound.Sound('a1.wav')
sound_1.setVolume(1)

# Initialize components for Routine "Questionnaire2"
Questionnaire2Clock = core.Clock()
questionnaire2 = visual.TextStim(win=win, ori=0, name='questionnaire2',
    text='default text',    font='Arial',
    units='pix', pos=[0,0], height=50, wrapWidth=1000,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "Text_Intro"
Text_IntroClock = core.Clock()
text_intro = visual.TextStim(win=win, ori=0, name='text_intro',
    text=u'Por favor, lee el siguiente texto cuidadosamente.\n\nAprieta cualquier boton para continuar.',    font=u'Arial',
    units='pix', pos=[0, 0], height=50, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "Text_Display"
Text_DisplayClock = core.Clock()
text_display = visual.TextStim(win=win, ori=0, name='text_display',
    text=u'A una ni\xf1a peque\xf1a llamada Maria le encanta pintar. En todos sus cuadros puedes encontrar algo de color amarillo, que es su color favorito. Hoy est\xe1 de pie delante de su caballete, llevando el pelo largo y negro atado en una coleta. Ella est\xe1 pintando un ramo de hermosas margaritas en un jarr\xf3n verde, cuando su madre Paula, grita a trav\xe9s de la casa: "\xa1La cena est\xe1 lista!" Pero Mar\xeda a\xfan no ha terminado su cuadro: "\xa1Cinco minutos m\xe1s!", ella grita. La madre entra en su habitaci\xf3n: "Si no comemos ya, la comida se enfriar\xe1." As\xed que Maria la sigue hasta la cocina. Su hermano Alejandro ya est\xe1 sentado en la mesa, jugando con su tablet. Alejandro es un poco m\xe1s alto que Maria, a pesar de que es dos a\xf1os menor que ella. \xc9l espera aburrido para que empiece la cena. La madre se est\xe1 poniendo sus guantes de cocina rojos para sacar el pollo del horno cuando el t\xedo de Mar\xeda, Carlos, entra en la cocina. \xc9l amablemente da unas palmaditas en la cabeza de Alejandro mientras camina detr\xe1s de Paula, d\xe1ndole un beso en la mejilla. Carlos se quita su chaqueta marr\xf3n y se sienta. Las paredes de la cocina est\xe1n llenos de cuadros de Mar\xeda y Carlos los admira cada vez que viene de visita. Maria est\xe1 tan entusiasmada que corre hacia su habitaci\xf3n para ense\xf1arle su \xfaltimo cuadro de flores a Carlos. Ella tambi\xe9n le dice que su pincel preferido est\xe1 roto, lo que hace proponer a Carlos a ir hacia la tienda el siguiente d\xeda para comprar uno nuevo. De repente, la t\xeda Laura entra bruscamente en la sala, llevando la noticia de que est\xe1 nevando. La familia entera corre afuera hacia el extra\xf1o evento. Solamente Alejandro se queda sentado adentro, impasiblemente observando la agitada familia. Todo indica que llegar\xe1n a la cena tarde. \xa1Otra vez!',    font='Arial',
    units='pix', pos=[0,0], height=50, wrapWidth=10000000,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "Questionnaire2"
Questionnaire2Clock = core.Clock()
questionnaire2 = visual.TextStim(win=win, ori=0, name='questionnaire2',
    text='default text',    font='Arial',
    units='pix', pos=[0,0], height=50, wrapWidth=1000,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "Thanks"
ThanksClock = core.Clock()
thanks = visual.TextStim(win=win, ori=0, name='thanks',
    text='Gracias por tu participacion!\n\nAprieta cualquier boton para finalizar.',    font='Arial',
    units='pix', pos=[0, 0], height=50, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "Start"-------
t = 0
StartClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_4.status = NOT_STARTED
# keep track of which components have finished
StartComponents = []
StartComponents.append(Start_Display)
StartComponents.append(key_resp_4)
for thisComponent in StartComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Start"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = StartClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Start_Display* updates
    if t >= 0.0 and Start_Display.status == NOT_STARTED:
        # keep track of start time/frame for later
        Start_Display.tStart = t  # underestimates by a little under one frame
        Start_Display.frameNStart = frameN  # exact frame index
        Start_Display.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t  # underestimates by a little under one frame
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        key_resp_4.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_4.keys = theseKeys[-1]  # just the last key pressed
            key_resp_4.rt = key_resp_4.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "Start"-------
for thisComponent in StartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
   key_resp_4.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.nextEntry()

#------Prepare to start Routine "Audio_Display"-------
t = 0
Audio_DisplayClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_3.status = NOT_STARTED
# keep track of which components have finished
Audio_DisplayComponents = []
Audio_DisplayComponents.append(sound_1)
Audio_DisplayComponents.append(key_resp_3)
for thisComponent in Audio_DisplayComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Audio_Display"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Audio_DisplayClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop sound_1
    if t >= 0.0 and sound_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        sound_1.tStart = t  # underestimates by a little under one frame
        sound_1.frameNStart = frameN  # exact frame index
        sound_1.play()  # start the sound (it finishes automatically)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t  # underestimates by a little under one frame
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['c'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Audio_DisplayComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "Audio_Display"-------
for thisComponent in Audio_DisplayComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
questions1 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath='C:\\Users\\dber\\Desktop\\Final_Experiment_PsychoPy-2014-11-26\\Final Experiment PsychoPy\\Group_B_Experiment.psyexp',
    trialList=data.importConditions('questionnaire_Marta.xlsx'),
    seed=None, name='questions1')
thisExp.addLoop(questions1)  # add the loop to the experiment
thisQuestions1 = questions1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisQuestions1.rgb)
if thisQuestions1 != None:
    for paramName in thisQuestions1.keys():
        exec(paramName + '= thisQuestions1.' + paramName)

for thisQuestions1 in questions1:
    currentLoop = questions1
    # abbreviate parameter names if possible (e.g. rgb = thisQuestions1.rgb)
    if thisQuestions1 != None:
        for paramName in thisQuestions1.keys():
            exec(paramName + '= thisQuestions1.' + paramName)
    
    #------Prepare to start Routine "Questionnaire2"-------
    t = 0
    Questionnaire2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    questionnaire2.setText(question+'\n\n1: '+answer1+'\n2: '+answer2+'\n3: '+answer3)
    key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_2.status = NOT_STARTED
    # keep track of which components have finished
    Questionnaire2Components = []
    Questionnaire2Components.append(questionnaire2)
    Questionnaire2Components.append(key_resp_2)
    for thisComponent in Questionnaire2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Questionnaire2"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = Questionnaire2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *questionnaire2* updates
        if t >= 0.0 and questionnaire2.status == NOT_STARTED:
            # keep track of start time/frame for later
            questionnaire2.tStart = t  # underestimates by a little under one frame
            questionnaire2.frameNStart = frameN  # exact frame index
            questionnaire2.setAutoDraw(True)
        
        # *key_resp_2* updates
        if t >= 0.0 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t  # underestimates by a little under one frame
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            key_resp_2.clock.reset()  # now t=0
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_2.keys.extend(theseKeys)  # storing all keys
                key_resp_2.rt.append(key_resp_2.clock.getTime())
                # was this 'correct'?
                if (key_resp_2.keys == str(correctAnswer)) or (key_resp_2.keys == correctAnswer):
                    key_resp_2.corr = 1
                else:
                    key_resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Questionnaire2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "Questionnaire2"-------
    for thisComponent in Questionnaire2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
       key_resp_2.keys=None
       # was no response the correct answer?!
       if str(correctAnswer).lower() == 'none': key_resp_2.corr = 1  # correct non-response
       else: key_resp_2.corr = 0  # failed to respond (incorrectly)
    # store data for questions1 (TrialHandler)
    questions1.addData('key_resp_2.keys',key_resp_2.keys)
    questions1.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        questions1.addData('key_resp_2.rt', key_resp_2.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'questions1'


#------Prepare to start Routine "Text_Intro"-------
t = 0
Text_IntroClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_5.status = NOT_STARTED
# keep track of which components have finished
Text_IntroComponents = []
Text_IntroComponents.append(text_intro)
Text_IntroComponents.append(key_resp_5)
for thisComponent in Text_IntroComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Text_Intro"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Text_IntroClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_intro* updates
    if t >= 0.0 and text_intro.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_intro.tStart = t  # underestimates by a little under one frame
        text_intro.frameNStart = frameN  # exact frame index
        text_intro.setAutoDraw(True)
    
    # *key_resp_5* updates
    if t >= 0.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t  # underestimates by a little under one frame
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.status = STARTED
        # keyboard checking is just starting
    if key_resp_5.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Text_IntroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "Text_Intro"-------
for thisComponent in Text_IntroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "Text_Display"-------
t = 0
Text_DisplayClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
quit_display = event.BuilderKeyResponse()  # create an object of type KeyResponse
quit_display.status = NOT_STARTED
# keep track of which components have finished
Text_DisplayComponents = []
Text_DisplayComponents.append(text_display)
Text_DisplayComponents.append(quit_display)
for thisComponent in Text_DisplayComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Text_Display"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Text_DisplayClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_display* updates
    if t >= 0.0 and text_display.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_display.tStart = t  # underestimates by a little under one frame
        text_display.frameNStart = frameN  # exact frame index
        text_display.setAutoDraw(True)
    elif text_display.status == STARTED and t >= (0.0 + (1000-win.monitorFramePeriod*0.75)): #most of one frame period left
        text_display.setAutoDraw(False)
    if text_display.status == STARTED:  # only update if being drawn
        text_display.setPos([20000-3*frameN, 50], log=False)
    
    # *quit_display* updates
    if t >= 0.0 and quit_display.status == NOT_STARTED:
        # keep track of start time/frame for later
        quit_display.tStart = t  # underestimates by a little under one frame
        quit_display.frameNStart = frameN  # exact frame index
        quit_display.status = STARTED
        # keyboard checking is just starting
    if quit_display.status == STARTED:
        theseKeys = event.getKeys(keyList=['c'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Text_DisplayComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "Text_Display"-------
for thisComponent in Text_DisplayComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
questions2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath='C:\\Users\\dber\\Desktop\\Final_Experiment_PsychoPy-2014-11-26\\Final Experiment PsychoPy\\Group_B_Experiment.psyexp',
    trialList=data.importConditions('questionnaire_Maria.xlsx'),
    seed=None, name='questions2')
thisExp.addLoop(questions2)  # add the loop to the experiment
thisQuestions2 = questions2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisQuestions2.rgb)
if thisQuestions2 != None:
    for paramName in thisQuestions2.keys():
        exec(paramName + '= thisQuestions2.' + paramName)

for thisQuestions2 in questions2:
    currentLoop = questions2
    # abbreviate parameter names if possible (e.g. rgb = thisQuestions2.rgb)
    if thisQuestions2 != None:
        for paramName in thisQuestions2.keys():
            exec(paramName + '= thisQuestions2.' + paramName)
    
    #------Prepare to start Routine "Questionnaire2"-------
    t = 0
    Questionnaire2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    questionnaire2.setText(question+'\n\n1: '+answer1+'\n2: '+answer2+'\n3: '+answer3)
    key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_2.status = NOT_STARTED
    # keep track of which components have finished
    Questionnaire2Components = []
    Questionnaire2Components.append(questionnaire2)
    Questionnaire2Components.append(key_resp_2)
    for thisComponent in Questionnaire2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Questionnaire2"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = Questionnaire2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *questionnaire2* updates
        if t >= 0.0 and questionnaire2.status == NOT_STARTED:
            # keep track of start time/frame for later
            questionnaire2.tStart = t  # underestimates by a little under one frame
            questionnaire2.frameNStart = frameN  # exact frame index
            questionnaire2.setAutoDraw(True)
        
        # *key_resp_2* updates
        if t >= 0.0 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t  # underestimates by a little under one frame
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            key_resp_2.clock.reset()  # now t=0
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_2.keys.extend(theseKeys)  # storing all keys
                key_resp_2.rt.append(key_resp_2.clock.getTime())
                # was this 'correct'?
                if (key_resp_2.keys == str(correctAnswer)) or (key_resp_2.keys == correctAnswer):
                    key_resp_2.corr = 1
                else:
                    key_resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Questionnaire2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "Questionnaire2"-------
    for thisComponent in Questionnaire2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
       key_resp_2.keys=None
       # was no response the correct answer?!
       if str(correctAnswer).lower() == 'none': key_resp_2.corr = 1  # correct non-response
       else: key_resp_2.corr = 0  # failed to respond (incorrectly)
    # store data for questions2 (TrialHandler)
    questions2.addData('key_resp_2.keys',key_resp_2.keys)
    questions2.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        questions2.addData('key_resp_2.rt', key_resp_2.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'questions2'


#------Prepare to start Routine "Thanks"-------
t = 0
ThanksClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
finsih = event.BuilderKeyResponse()  # create an object of type KeyResponse
finsih.status = NOT_STARTED
# keep track of which components have finished
ThanksComponents = []
ThanksComponents.append(thanks)
ThanksComponents.append(finsih)
for thisComponent in ThanksComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Thanks"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = ThanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanks* updates
    if t >= 0.0 and thanks.status == NOT_STARTED:
        # keep track of start time/frame for later
        thanks.tStart = t  # underestimates by a little under one frame
        thanks.frameNStart = frameN  # exact frame index
        thanks.setAutoDraw(True)
    
    # *finsih* updates
    if t >= 0.0 and finsih.status == NOT_STARTED:
        # keep track of start time/frame for later
        finsih.tStart = t  # underestimates by a little under one frame
        finsih.frameNStart = frameN  # exact frame index
        finsih.status = STARTED
        # keyboard checking is just starting
        finsih.clock.reset()  # now t=0
    if finsih.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            finsih.keys = theseKeys[-1]  # just the last key pressed
            finsih.rt = finsih.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ThanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "Thanks"-------
for thisComponent in ThanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if finsih.keys in ['', [], None]:  # No response was made
   finsih.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('finsih.keys',finsih.keys)
if finsih.keys != None:  # we had a response
    thisExp.addData('finsih.rt', finsih.rt)
thisExp.nextEntry()
win.close()
core.quit()
