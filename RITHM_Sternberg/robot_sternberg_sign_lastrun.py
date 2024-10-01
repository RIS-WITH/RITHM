#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on août 29, 2024, at 11:29
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from translations
langage = None

base_txt = [
 'intro',
 'Training with letter condition and',
 'Training with robot condition and',
 'letter condition',
 'robot condition',
 'Item presented during the sequence ?',
 '[c]orrect',
 '[n]ot correct',
 'Press space to confirm',
 'Press space to begin',
 'Are you ready to begin the experiment ?',
 'Block',
 '',
 'Absolutely no effort',
 'Almost no effort',
 'A little effort',
 'Some effort',
 'Rather much effort',
 'Considerable effort',
 'Great effort',
 'Very great effort',
 'Extreme effort',
 'Indicate your cognitive effort level by cliking on the scale',
 ]

langage_mapping = {'e':'en', 'f':'fr'}

langages = {

'en':{
 'intro': 'Welcome to the Stenberg task!\n\nIn this task, you will be presented with a sequence of 2, 4 or 6 items, whether letters or videos. Then, a letter or video will be displayed and you will be asked whether it appeared in the presented sequence.\n\nPress C for [c]orrect or N for [n]ot correct.\n\nYou will also be asked to tell us how difficult you perceived the task to be, ranging from Absolutely no effort (2) to Extreme effort (112).\n\nPress space to begin!',
 'Training with letter condition and':'Training with letter condition and',
 'Training with robot condition and':'Training with robot condition and',
 'letter condition':'letter condition',
 'robot condition':'robot condition',
 'Item presented during the sequence ?':'Item presented during the sequence ?',
 '[c]orrect': '[c]orrect',
 '[n]ot correct': '[n]ot correct',
 'Press space to confirm': 'Press space to confirm',
 'Press space to begin': 'Press space to begin',
 'Are you ready to begin the experiment ?': 'Are you ready to begin the experiment ?',
 'Block': 'Block',
 '': '',
 'Absolutely no effort': 'Absolutely no effort',
 'Almost no effort': 'Almost no effort',
 'A little effort': 'A little effort',
 'Some effort': 'Some effort',
 'Rather much effort': 'Rather much effort',
 'Considerable effort': 'Considerable effort',
 'Great effort': 'Great effort',
 'Very great effort': 'Very great effort',
 'Extreme effort': 'Extreme effort',
 'Indicate your cognitive effort level by cliking on the scale': 'Indicate your cognitive effort level by cliking on the scale',
 },


'fr':{
 'intro': "Bienvenue à la tâche de Stenberg !\n\nDans cette tâche, une séquence de 2, 4 ou 6 items vous sera présentée, qu’il s’agisse de lettres ou de vidéos. Ensuite, une lettre ou une vidéo s’affichera et vous devrez déterminer si elle était apparue dans la séquence présentée.\n\nAppuyez sur C pour [c]orrect ou N pour [n]on correct.\n\nOn vous demandera également d'évaluer la difficulté perçue de la tâche, allant de Absolument aucun effort (2) à Effort extrême (112) \n\nAppuyez sur espace pour commencer !",
 'Training with letter condition and':'Entraînement avec la condition lettre et',
 'Training with robot condition and':'Entraînement avec la condition robot et',
 'letter condition':'condition lettre',
 'robot condition':'condition robot',
 'Item presented during the sequence ?':'Item présenté pendant la séquence ?',
 '[c]orrect': '[c]orrect',
 '[n]ot correct': '[n]on correct',
 'Press space to confirm': 'Appuyez sur espace pour confirmer',
 'Press space to begin': 'Appuyez sur espace pour commencer',
 'Are you ready to begin the experiment ?': "Êtes vous prêt à commencer l'expérience ?",
 'Block': 'Bloc',
 '': '',
 'Absolutely no effort': 'Absolument aucun effort',
 'Almost no effort': 'Presque aucun effort',
 'A little effort': "Un petit effort",
 'Some effort': "Des efforts",
 'Rather much effort': "Beaucoup d'effort",
 'Considerable effort': 'Effort considérable',
 'Great effort': 'Grand effort',
 'Very great effort': 'Très grand effort',
 'Extreme effort': 'Effort extrême',
 'Indicate your cognitive effort level by cliking on the scale': "Indiquez votre niveau d'effort cognitif en cliquant sur l'échelle",
 },

}


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'robot_sternberg_sign'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/subject_%s/%s_%s_%s' % (expInfo['participant'], expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\a.sanmarti-decool\\Documents\\RITHM_Sternberg\\robot_sternberg_sign_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1680, 1050], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "langage_selection" ---
langage_text = visual.TextStim(win=win, name='langage_text',
    text="Press (E) to do the experiment in English \n\nAppuyez sur (F) pour faire l'expérience en français",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
langage_key = keyboard.Keyboard()

# --- Initialize components for Routine "intro" ---
intro_text = visual.TextStim(win=win, name='intro_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
intro_key = keyboard.Keyboard()

# --- Initialize components for Routine "training_intro" ---
training_intro_text = visual.TextStim(win=win, name='training_intro_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
training_intro_key = keyboard.Keyboard()

# --- Initialize components for Routine "fixation" ---
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "training_presentation" ---
training_presentation_letter = visual.TextStim(win=win, name='training_presentation_letter',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "fixation" ---
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "training_recall" ---
training_recall_letter = visual.TextStim(win=win, name='training_recall_letter',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
training_recall_key = keyboard.Keyboard()
training_recall_question = visual.TextStim(win=win, name='training_recall_question',
    text='',
    font='Open Sans',
    pos=(0, 0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
training_recall_answer = visual.TextStim(win=win, name='training_recall_answer',
    text='',
    font='Open Sans',
    pos=(0.03, -0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "block_questionnaire" ---
RSME_labels = visual.Slider(win=win, name='RSME_labels',
    startValue=None, size=(0.9, 0.02), pos=(-0.3, 0.02), units=None,
    labels=("", "Absolutely no effort", "Almost no effort", "A little effort", "Some effort", "Rather much effort", "Considerable effort", "Great effort", "Very great effort", "Extreme effort", ""), ticks=(0, 2,13,25,37,57,71,85,102,112, 150), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.02,
    flip=True, ori=90.0, depth=0, readOnly=True)
RSME_ticks = visual.Slider(win=win, name='RSME_ticks',
    startValue=None, size=(0.9, 0.03), pos=(-0.3, 0.02), units=None,
    labels=(0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150), ticks=(0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150), granularity=0.0,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, ori=90.0, depth=-1, readOnly=False)
RSME_text = visual.TextStim(win=win, name='RSME_text',
    text='',
    font='Open Sans',
    pos=(0.4, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
RSME_key = keyboard.Keyboard()

# --- Initialize components for Routine "experiment_beginning" ---
experiment_beginning_text = visual.TextStim(win=win, name='experiment_beginning_text',
    text='Are you ready to begin the experiment ?',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
experiment_beginning_keys = visual.TextStim(win=win, name='experiment_beginning_keys',
    text='[c]orrect                    [n]ot correct',
    font='Open Sans',
    pos=(0.03, -0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
experiment_beginning_key = keyboard.Keyboard()

# --- Initialize components for Routine "block_intro" ---
block_intro_text = visual.TextStim(win=win, name='block_intro_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
block_intro_key = keyboard.Keyboard()

# --- Initialize components for Routine "fixation" ---
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "presentation" ---
presentation_letter = visual.TextStim(win=win, name='presentation_letter',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "fixation" ---
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "recall" ---
recall_letter = visual.TextStim(win=win, name='recall_letter',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
recall_key = keyboard.Keyboard()
recall_question = visual.TextStim(win=win, name='recall_question',
    text='',
    font='Open Sans',
    pos=(0, 0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
recall_answer = visual.TextStim(win=win, name='recall_answer',
    text='',
    font='Open Sans',
    pos=(0.03, -0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "block_questionnaire" ---
RSME_labels = visual.Slider(win=win, name='RSME_labels',
    startValue=None, size=(0.9, 0.02), pos=(-0.3, 0.02), units=None,
    labels=("", "Absolutely no effort", "Almost no effort", "A little effort", "Some effort", "Rather much effort", "Considerable effort", "Great effort", "Very great effort", "Extreme effort", ""), ticks=(0, 2,13,25,37,57,71,85,102,112, 150), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.02,
    flip=True, ori=90.0, depth=0, readOnly=True)
RSME_ticks = visual.Slider(win=win, name='RSME_ticks',
    startValue=None, size=(0.9, 0.03), pos=(-0.3, 0.02), units=None,
    labels=(0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150), ticks=(0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150), granularity=0.0,
    style='rating', styleTweaks=('triangleMarker',), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, ori=90.0, depth=-1, readOnly=False)
RSME_text = visual.TextStim(win=win, name='RSME_text',
    text='',
    font='Open Sans',
    pos=(0.4, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
RSME_key = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "langage_selection" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
langage_key.keys = []
langage_key.rt = []
_langage_key_allKeys = []
# keep track of which components have finished
langage_selectionComponents = [langage_text, langage_key]
for thisComponent in langage_selectionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "langage_selection" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *langage_text* updates
    if langage_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        langage_text.frameNStart = frameN  # exact frame index
        langage_text.tStart = t  # local t and not account for scr refresh
        langage_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(langage_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'langage_text.started')
        langage_text.setAutoDraw(True)
    
    # *langage_key* updates
    waitOnFlip = False
    if langage_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        langage_key.frameNStart = frameN  # exact frame index
        langage_key.tStart = t  # local t and not account for scr refresh
        langage_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(langage_key, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'langage_key.started')
        langage_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(langage_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(langage_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if langage_key.status == STARTED and not waitOnFlip:
        theseKeys = langage_key.getKeys(keyList=['e', 'f'], waitRelease=False)
        _langage_key_allKeys.extend(theseKeys)
        if len(_langage_key_allKeys):
            langage_key.keys = _langage_key_allKeys[-1].name  # just the last key pressed
            langage_key.rt = _langage_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in langage_selectionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "langage_selection" ---
for thisComponent in langage_selectionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if langage_key.keys in ['', [], None]:  # No response was made
    langage_key.keys = None
thisExp.addData('langage_key.keys',langage_key.keys)
if langage_key.keys != None:  # we had a response
    thisExp.addData('langage_key.rt', langage_key.rt)
thisExp.nextEntry()
# Run 'End Routine' code from init_code
langage = langages[langage_mapping[langage_key.keys]]
subject_dir = f"data\\subject_{expInfo['participant']}"
# the Routine "langage_selection" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "intro" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
intro_text.setText(f"{langage['intro']}")
intro_key.keys = []
intro_key.rt = []
_intro_key_allKeys = []
# keep track of which components have finished
introComponents = [intro_text, intro_key]
for thisComponent in introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "intro" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro_text* updates
    if intro_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_text.frameNStart = frameN  # exact frame index
        intro_text.tStart = t  # local t and not account for scr refresh
        intro_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'intro_text.started')
        intro_text.setAutoDraw(True)
    
    # *intro_key* updates
    waitOnFlip = False
    if intro_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_key.frameNStart = frameN  # exact frame index
        intro_key.tStart = t  # local t and not account for scr refresh
        intro_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_key, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'intro_key.started')
        intro_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(intro_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(intro_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if intro_key.status == STARTED and not waitOnFlip:
        theseKeys = intro_key.getKeys(keyList=['space'], waitRelease=False)
        _intro_key_allKeys.extend(theseKeys)
        if len(_intro_key_allKeys):
            intro_key.keys = _intro_key_allKeys[-1].name  # just the last key pressed
            intro_key.rt = _intro_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "intro" ---
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if intro_key.keys in ['', [], None]:  # No response was made
    intro_key.keys = None
thisExp.addData('intro_key.keys',intro_key.keys)
if intro_key.keys != None:  # we had a response
    thisExp.addData('intro_key.rt', intro_key.rt)
thisExp.nextEntry()
# the Routine "intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
retraining = data.TrialHandler(nReps=50.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='retraining')
thisExp.addLoop(retraining)  # add the loop to the experiment
thisRetraining = retraining.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRetraining.rgb)
if thisRetraining != None:
    for paramName in thisRetraining:
        exec('{} = thisRetraining[paramName]'.format(paramName))

for thisRetraining in retraining:
    currentLoop = retraining
    # abbreviate parameter names if possible (e.g. rgb = thisRetraining.rgb)
    if thisRetraining != None:
        for paramName in thisRetraining:
            exec('{} = thisRetraining[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    training = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(f"{subject_dir}\\conditions_sternberg_short.csv"),
        seed=None, name='training')
    thisExp.addLoop(training)  # add the loop to the experiment
    thisTraining = training.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTraining.rgb)
    if thisTraining != None:
        for paramName in thisTraining:
            exec('{} = thisTraining[paramName]'.format(paramName))
    
    for thisTraining in training:
        currentLoop = training
        # abbreviate parameter names if possible (e.g. rgb = thisTraining.rgb)
        if thisTraining != None:
            for paramName in thisTraining:
                exec('{} = thisTraining[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "training_intro" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        training_intro_text.setText(f"{langage[f'Training with {stimuli} condition and']} {condition} items \n\n{langage['Press space to begin']}")
        training_intro_key.keys = []
        training_intro_key.rt = []
        _training_intro_key_allKeys = []
        # keep track of which components have finished
        training_introComponents = [training_intro_text, training_intro_key]
        for thisComponent in training_introComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "training_intro" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *training_intro_text* updates
            if training_intro_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                training_intro_text.frameNStart = frameN  # exact frame index
                training_intro_text.tStart = t  # local t and not account for scr refresh
                training_intro_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(training_intro_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'training_intro_text.started')
                training_intro_text.setAutoDraw(True)
            if training_intro_text.status == STARTED:
                if bool(is_block_beginning==False):
                    # keep track of stop time/frame for later
                    training_intro_text.tStop = t  # not accounting for scr refresh
                    training_intro_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'training_intro_text.stopped')
                    training_intro_text.setAutoDraw(False)
            
            # *training_intro_key* updates
            waitOnFlip = False
            if training_intro_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                training_intro_key.frameNStart = frameN  # exact frame index
                training_intro_key.tStart = t  # local t and not account for scr refresh
                training_intro_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(training_intro_key, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'training_intro_key.started')
                training_intro_key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(training_intro_key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(training_intro_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if training_intro_key.status == STARTED:
                if bool(is_block_beginning==False):
                    # keep track of stop time/frame for later
                    training_intro_key.tStop = t  # not accounting for scr refresh
                    training_intro_key.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'training_intro_key.stopped')
                    training_intro_key.status = FINISHED
            if training_intro_key.status == STARTED and not waitOnFlip:
                theseKeys = training_intro_key.getKeys(keyList=['space'], waitRelease=False)
                _training_intro_key_allKeys.extend(theseKeys)
                if len(_training_intro_key_allKeys):
                    training_intro_key.keys = _training_intro_key_allKeys[-1].name  # just the last key pressed
                    training_intro_key.rt = _training_intro_key_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in training_introComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "training_intro" ---
        for thisComponent in training_introComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if training_intro_key.keys in ['', [], None]:  # No response was made
            training_intro_key.keys = None
        training.addData('training_intro_key.keys',training_intro_key.keys)
        if training_intro_key.keys != None:  # we had a response
            training.addData('training_intro_key.rt', training_intro_key.rt)
        # the Routine "training_intro" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "fixation" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        fixationComponents = [polygon]
        for thisComponent in fixationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fixation" ---
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon* updates
            if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon.frameNStart = frameN  # exact frame index
                polygon.tStart = t  # local t and not account for scr refresh
                polygon.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon.started')
                polygon.setAutoDraw(True)
            if polygon.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon.tStop = t  # not accounting for scr refresh
                    polygon.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon.stopped')
                    polygon.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixation" ---
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # set up handler to look after randomisation of conditions etc
        training_sequence_loop = data.TrialHandler(nReps=50.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='training_sequence_loop')
        thisExp.addLoop(training_sequence_loop)  # add the loop to the experiment
        thisTraining_sequence_loop = training_sequence_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTraining_sequence_loop.rgb)
        if thisTraining_sequence_loop != None:
            for paramName in thisTraining_sequence_loop:
                exec('{} = thisTraining_sequence_loop[paramName]'.format(paramName))
        
        for thisTraining_sequence_loop in training_sequence_loop:
            currentLoop = training_sequence_loop
            # abbreviate parameter names if possible (e.g. rgb = thisTraining_sequence_loop.rgb)
            if thisTraining_sequence_loop != None:
                for paramName in thisTraining_sequence_loop:
                    exec('{} = thisTraining_sequence_loop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "training_presentation" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            training_presentation_movie = visual.MovieStim(
                win=win, name='training_presentation_movie', units='',
                noAudio=True,
                filename=sequence_fnames[training_sequence_loop.thisN],
                ori=0.0, pos=(0, 0), opacity=None,
                loop=False, anchor='center',
                size=(0.3,0.5),
                depth=0.0,
                )
            training_presentation_letter.setText(sequence[training_sequence_loop.thisN])
            # keep track of which components have finished
            training_presentationComponents = [training_presentation_movie, training_presentation_letter]
            for thisComponent in training_presentationComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "training_presentation" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *training_presentation_movie* updates
                if training_presentation_movie.status == NOT_STARTED and len(sequence[training_sequence_loop.thisN])>1:
                    # keep track of start time/frame for later
                    training_presentation_movie.frameNStart = frameN  # exact frame index
                    training_presentation_movie.tStart = t  # local t and not account for scr refresh
                    training_presentation_movie.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(training_presentation_movie, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'training_presentation_movie.started')
                    training_presentation_movie.setAutoDraw(True)
                    training_presentation_movie.play()
                if training_presentation_movie.status == FINISHED:  # force-end the routine
                    continueRoutine = False
                
                # *training_presentation_letter* updates
                if training_presentation_letter.status == NOT_STARTED and len(sequence[training_sequence_loop.thisN])==1:
                    # keep track of start time/frame for later
                    training_presentation_letter.frameNStart = frameN  # exact frame index
                    training_presentation_letter.tStart = t  # local t and not account for scr refresh
                    training_presentation_letter.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(training_presentation_letter, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'training_presentation_letter.started')
                    training_presentation_letter.setAutoDraw(True)
                if training_presentation_letter.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > training_presentation_letter.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        training_presentation_letter.tStop = t  # not accounting for scr refresh
                        training_presentation_letter.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'training_presentation_letter.stopped')
                        training_presentation_letter.setAutoDraw(False)
                # Run 'Each Frame' code from training_presentation_letter_force_end
                if training_presentation_letter.status == FINISHED:
                    continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in training_presentationComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "training_presentation" ---
            for thisComponent in training_presentationComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            training_presentation_movie.stop()
            # Run 'End Routine' code from end_training_presentation_sequence
            next_N = training_sequence_loop.thisN + 1
            if next_N >= len(sequence_fnames):
                training_sequence_loop.finished = True
            # the Routine "training_presentation" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
        # completed 50.0 repeats of 'training_sequence_loop'
        
        
        # --- Prepare to start Routine "fixation" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        fixationComponents = [polygon]
        for thisComponent in fixationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fixation" ---
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon* updates
            if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon.frameNStart = frameN  # exact frame index
                polygon.tStart = t  # local t and not account for scr refresh
                polygon.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon.started')
                polygon.setAutoDraw(True)
            if polygon.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon.tStop = t  # not accounting for scr refresh
                    polygon.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon.stopped')
                    polygon.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixation" ---
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "training_recall" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        training_recall_letter.setText(target)
        training_recall_movie = visual.MovieStim(
            win=win, name='training_recall_movie', units='',
            noAudio=True,
            filename=target_fname,
            ori=0.0, pos=(0, 0), opacity=None,
            loop=False, anchor='center',
            size=(0.3,0.5),
            depth=-1.0,
            )
        training_recall_key.keys = []
        training_recall_key.rt = []
        _training_recall_key_allKeys = []
        training_recall_question.setText(langage['Item presented during the sequence ?'])
        training_recall_answer.setText(f"{langage['[c]orrect']}                    {langage['[n]ot correct']}")
        # keep track of which components have finished
        training_recallComponents = [training_recall_letter, training_recall_movie, training_recall_key, training_recall_question, training_recall_answer]
        for thisComponent in training_recallComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "training_recall" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *training_recall_letter* updates
            if training_recall_letter.status == NOT_STARTED and len(target)==1:
                # keep track of start time/frame for later
                training_recall_letter.frameNStart = frameN  # exact frame index
                training_recall_letter.tStart = t  # local t and not account for scr refresh
                training_recall_letter.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(training_recall_letter, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'training_recall_letter.started')
                training_recall_letter.setAutoDraw(True)
            
            # *training_recall_movie* updates
            if training_recall_movie.status == NOT_STARTED and len(target)>1:
                # keep track of start time/frame for later
                training_recall_movie.frameNStart = frameN  # exact frame index
                training_recall_movie.tStart = t  # local t and not account for scr refresh
                training_recall_movie.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(training_recall_movie, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'training_recall_movie.started')
                training_recall_movie.setAutoDraw(True)
                training_recall_movie.play()
            
            # *training_recall_key* updates
            waitOnFlip = False
            if training_recall_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                training_recall_key.frameNStart = frameN  # exact frame index
                training_recall_key.tStart = t  # local t and not account for scr refresh
                training_recall_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(training_recall_key, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'training_recall_key.started')
                training_recall_key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(training_recall_key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(training_recall_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if training_recall_key.status == STARTED and not waitOnFlip:
                theseKeys = training_recall_key.getKeys(keyList=['c', 'n'], waitRelease=False)
                _training_recall_key_allKeys.extend(theseKeys)
                if len(_training_recall_key_allKeys):
                    training_recall_key.keys = _training_recall_key_allKeys[-1].name  # just the last key pressed
                    training_recall_key.rt = _training_recall_key_allKeys[-1].rt
            
            # *training_recall_question* updates
            if training_recall_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                training_recall_question.frameNStart = frameN  # exact frame index
                training_recall_question.tStart = t  # local t and not account for scr refresh
                training_recall_question.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(training_recall_question, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'training_recall_question.started')
                training_recall_question.setAutoDraw(True)
            
            # *training_recall_answer* updates
            if training_recall_answer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                training_recall_answer.frameNStart = frameN  # exact frame index
                training_recall_answer.tStart = t  # local t and not account for scr refresh
                training_recall_answer.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(training_recall_answer, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'training_recall_answer.started')
                training_recall_answer.setAutoDraw(True)
            # Run 'Each Frame' code from end_training_recall_routine
            if (training_recall_movie.isFinished or len(target)==1) and len(training_recall_key.keys)>0:
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in training_recallComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "training_recall" ---
        for thisComponent in training_recallComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        training_recall_movie.stop()
        # check responses
        if training_recall_key.keys in ['', [], None]:  # No response was made
            training_recall_key.keys = None
        training.addData('training_recall_key.keys',training_recall_key.keys)
        if training_recall_key.keys != None:  # we had a response
            training.addData('training_recall_key.rt', training_recall_key.rt)
        # the Routine "training_recall" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "block_questionnaire" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        RSME_labels.reset()
        RSME_ticks.reset()
        RSME_text.setText(f"{langage['Indicate your cognitive effort level by cliking on the scale']}\n\n{langage['Press space to confirm']}")
        RSME_key.keys = []
        RSME_key.rt = []
        _RSME_key_allKeys = []
        # Run 'Begin Routine' code from label_translation
        labels = [langage[label] if label in base_txt else label for label in RSME_labels.labels]
        RSME_labels.labels = labels
        for i, obj in enumerate(RSME_labels.labelObjs):
            # ...set its text to be the corresponding value in labels, and store this in the slider
            obj.text = RSME_labels.labels[i]
        # keep track of which components have finished
        block_questionnaireComponents = [RSME_labels, RSME_ticks, RSME_text, RSME_key]
        for thisComponent in block_questionnaireComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "block_questionnaire" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *RSME_labels* updates
            if RSME_labels.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                RSME_labels.frameNStart = frameN  # exact frame index
                RSME_labels.tStart = t  # local t and not account for scr refresh
                RSME_labels.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(RSME_labels, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RSME_labels.started')
                RSME_labels.setAutoDraw(True)
            if RSME_labels.status == STARTED:
                if bool(is_block_ending==False or (RSME_key.rt!=[] and RSME_ticks.rt!=None and RSME_key.rt > RSME_ticks.rt)):
                    # keep track of stop time/frame for later
                    RSME_labels.tStop = t  # not accounting for scr refresh
                    RSME_labels.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'RSME_labels.stopped')
                    RSME_labels.setAutoDraw(False)
            
            # *RSME_ticks* updates
            if RSME_ticks.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                RSME_ticks.frameNStart = frameN  # exact frame index
                RSME_ticks.tStart = t  # local t and not account for scr refresh
                RSME_ticks.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(RSME_ticks, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RSME_ticks.started')
                RSME_ticks.setAutoDraw(True)
            if RSME_ticks.status == STARTED:
                if bool(is_block_ending==False or (RSME_key.rt!=[] and RSME_ticks.rt!=None and RSME_key.rt > RSME_ticks.rt)):
                    # keep track of stop time/frame for later
                    RSME_ticks.tStop = t  # not accounting for scr refresh
                    RSME_ticks.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'RSME_ticks.stopped')
                    RSME_ticks.setAutoDraw(False)
            
            # *RSME_text* updates
            if RSME_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                RSME_text.frameNStart = frameN  # exact frame index
                RSME_text.tStart = t  # local t and not account for scr refresh
                RSME_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(RSME_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RSME_text.started')
                RSME_text.setAutoDraw(True)
            if RSME_text.status == STARTED:
                if bool(is_block_ending==False or (RSME_key.rt!=[] and RSME_ticks.rt!=None and RSME_key.rt > RSME_ticks.rt)):
                    # keep track of stop time/frame for later
                    RSME_text.tStop = t  # not accounting for scr refresh
                    RSME_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'RSME_text.stopped')
                    RSME_text.setAutoDraw(False)
            
            # *RSME_key* updates
            waitOnFlip = False
            if RSME_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                RSME_key.frameNStart = frameN  # exact frame index
                RSME_key.tStart = t  # local t and not account for scr refresh
                RSME_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(RSME_key, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RSME_key.started')
                RSME_key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(RSME_key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(RSME_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if RSME_key.status == STARTED:
                if bool(is_block_ending==False or (RSME_key.rt!=[] and RSME_ticks.rt!=None and RSME_key.rt > RSME_ticks.rt)):
                    # keep track of stop time/frame for later
                    RSME_key.tStop = t  # not accounting for scr refresh
                    RSME_key.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'RSME_key.stopped')
                    RSME_key.status = FINISHED
            if RSME_key.status == STARTED and not waitOnFlip:
                theseKeys = RSME_key.getKeys(keyList=['space'], waitRelease=False)
                _RSME_key_allKeys.extend(theseKeys)
                if len(_RSME_key_allKeys):
                    RSME_key.keys = _RSME_key_allKeys[-1].name  # just the last key pressed
                    RSME_key.rt = _RSME_key_allKeys[-1].rt
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in block_questionnaireComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "block_questionnaire" ---
        for thisComponent in block_questionnaireComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        training.addData('RSME_ticks.response', RSME_ticks.getRating())
        training.addData('RSME_ticks.rt', RSME_ticks.getRT())
        # check responses
        if RSME_key.keys in ['', [], None]:  # No response was made
            RSME_key.keys = None
        training.addData('RSME_key.keys',RSME_key.keys)
        if RSME_key.keys != None:  # we had a response
            training.addData('RSME_key.rt', RSME_key.rt)
        # the Routine "block_questionnaire" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'training'
    
    
    # --- Prepare to start Routine "experiment_beginning" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    experiment_beginning_key.keys = []
    experiment_beginning_key.rt = []
    _experiment_beginning_key_allKeys = []
    # keep track of which components have finished
    experiment_beginningComponents = [experiment_beginning_text, experiment_beginning_keys, experiment_beginning_key]
    for thisComponent in experiment_beginningComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "experiment_beginning" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *experiment_beginning_text* updates
        if experiment_beginning_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            experiment_beginning_text.frameNStart = frameN  # exact frame index
            experiment_beginning_text.tStart = t  # local t and not account for scr refresh
            experiment_beginning_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(experiment_beginning_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'experiment_beginning_text.started')
            experiment_beginning_text.setAutoDraw(True)
        
        # *experiment_beginning_keys* updates
        if experiment_beginning_keys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            experiment_beginning_keys.frameNStart = frameN  # exact frame index
            experiment_beginning_keys.tStart = t  # local t and not account for scr refresh
            experiment_beginning_keys.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(experiment_beginning_keys, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'experiment_beginning_keys.started')
            experiment_beginning_keys.setAutoDraw(True)
        
        # *experiment_beginning_key* updates
        waitOnFlip = False
        if experiment_beginning_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            experiment_beginning_key.frameNStart = frameN  # exact frame index
            experiment_beginning_key.tStart = t  # local t and not account for scr refresh
            experiment_beginning_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(experiment_beginning_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'experiment_beginning_key.started')
            experiment_beginning_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(experiment_beginning_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(experiment_beginning_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if experiment_beginning_key.status == STARTED and not waitOnFlip:
            theseKeys = experiment_beginning_key.getKeys(keyList=['c', 'n'], waitRelease=False)
            _experiment_beginning_key_allKeys.extend(theseKeys)
            if len(_experiment_beginning_key_allKeys):
                experiment_beginning_key.keys = _experiment_beginning_key_allKeys[-1].name  # just the last key pressed
                experiment_beginning_key.rt = _experiment_beginning_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in experiment_beginningComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "experiment_beginning" ---
    for thisComponent in experiment_beginningComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if experiment_beginning_key.keys in ['', [], None]:  # No response was made
        experiment_beginning_key.keys = None
    retraining.addData('experiment_beginning_key.keys',experiment_beginning_key.keys)
    if experiment_beginning_key.keys != None:  # we had a response
        retraining.addData('experiment_beginning_key.rt', experiment_beginning_key.rt)
    # Run 'End Routine' code from conditional_loop
    if experiment_beginning_key.keys[0] == 'c':
        retraining.finished = True
        
    # the Routine "experiment_beginning" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 50.0 repeats of 'retraining'


# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(f"{subject_dir}\\conditions_sternberg.csv"),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "block_intro" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    block_intro_text.setText(f"{langage['Block']} {block} {langage[f'{stimuli} condition']} {condition} items \n\n{langage['Press space to begin']}")
    block_intro_key.keys = []
    block_intro_key.rt = []
    _block_intro_key_allKeys = []
    # keep track of which components have finished
    block_introComponents = [block_intro_text, block_intro_key]
    for thisComponent in block_introComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "block_intro" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *block_intro_text* updates
        if block_intro_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block_intro_text.frameNStart = frameN  # exact frame index
            block_intro_text.tStart = t  # local t and not account for scr refresh
            block_intro_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block_intro_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block_intro_text.started')
            block_intro_text.setAutoDraw(True)
        if block_intro_text.status == STARTED:
            if bool(is_block_beginning==False):
                # keep track of stop time/frame for later
                block_intro_text.tStop = t  # not accounting for scr refresh
                block_intro_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block_intro_text.stopped')
                block_intro_text.setAutoDraw(False)
        
        # *block_intro_key* updates
        waitOnFlip = False
        if block_intro_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block_intro_key.frameNStart = frameN  # exact frame index
            block_intro_key.tStart = t  # local t and not account for scr refresh
            block_intro_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block_intro_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'block_intro_key.started')
            block_intro_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(block_intro_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(block_intro_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if block_intro_key.status == STARTED:
            if bool(is_block_beginning==False):
                # keep track of stop time/frame for later
                block_intro_key.tStop = t  # not accounting for scr refresh
                block_intro_key.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'block_intro_key.stopped')
                block_intro_key.status = FINISHED
        if block_intro_key.status == STARTED and not waitOnFlip:
            theseKeys = block_intro_key.getKeys(keyList=['space'], waitRelease=False)
            _block_intro_key_allKeys.extend(theseKeys)
            if len(_block_intro_key_allKeys):
                block_intro_key.keys = _block_intro_key_allKeys[-1].name  # just the last key pressed
                block_intro_key.rt = _block_intro_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block_introComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "block_intro" ---
    for thisComponent in block_introComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if block_intro_key.keys in ['', [], None]:  # No response was made
        block_intro_key.keys = None
    trials.addData('block_intro_key.keys',block_intro_key.keys)
    if block_intro_key.keys != None:  # we had a response
        trials.addData('block_intro_key.rt', block_intro_key.rt)
    # the Routine "block_intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "fixation" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationComponents = [polygon]
    for thisComponent in fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "fixation" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon.started')
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon.stopped')
                polygon.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fixation" ---
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # set up handler to look after randomisation of conditions etc
    sequence_loop = data.TrialHandler(nReps=50.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='sequence_loop')
    thisExp.addLoop(sequence_loop)  # add the loop to the experiment
    thisSequence_loop = sequence_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSequence_loop.rgb)
    if thisSequence_loop != None:
        for paramName in thisSequence_loop:
            exec('{} = thisSequence_loop[paramName]'.format(paramName))
    
    for thisSequence_loop in sequence_loop:
        currentLoop = sequence_loop
        # abbreviate parameter names if possible (e.g. rgb = thisSequence_loop.rgb)
        if thisSequence_loop != None:
            for paramName in thisSequence_loop:
                exec('{} = thisSequence_loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "presentation" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        presentation_movie = visual.MovieStim(
            win=win, name='presentation_movie', units='',
            noAudio=True,
            filename=sequence_fnames[sequence_loop.thisN],
            ori=0.0, pos=(0, 0), opacity=None,
            loop=False, anchor='center',
            size=(0.3,0.5),
            depth=0.0,
            )
        presentation_letter.setText(sequence[sequence_loop.thisN])
        # keep track of which components have finished
        presentationComponents = [presentation_movie, presentation_letter]
        for thisComponent in presentationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "presentation" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *presentation_movie* updates
            if presentation_movie.status == NOT_STARTED and len(sequence[sequence_loop.thisN])>1:
                # keep track of start time/frame for later
                presentation_movie.frameNStart = frameN  # exact frame index
                presentation_movie.tStart = t  # local t and not account for scr refresh
                presentation_movie.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(presentation_movie, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'presentation_movie.started')
                presentation_movie.setAutoDraw(True)
                presentation_movie.play()
            if presentation_movie.status == FINISHED:  # force-end the routine
                continueRoutine = False
            
            # *presentation_letter* updates
            if presentation_letter.status == NOT_STARTED and len(sequence[sequence_loop.thisN])==1:
                # keep track of start time/frame for later
                presentation_letter.frameNStart = frameN  # exact frame index
                presentation_letter.tStart = t  # local t and not account for scr refresh
                presentation_letter.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(presentation_letter, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'presentation_letter.started')
                presentation_letter.setAutoDraw(True)
            if presentation_letter.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > presentation_letter.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    presentation_letter.tStop = t  # not accounting for scr refresh
                    presentation_letter.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'presentation_letter.stopped')
                    presentation_letter.setAutoDraw(False)
            # Run 'Each Frame' code from presentation_letter_force_end
            if presentation_letter.status == FINISHED:
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in presentationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "presentation" ---
        for thisComponent in presentationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        presentation_movie.stop()
        # Run 'End Routine' code from end_presentation_sequence
        next_N = sequence_loop.thisN + 1
        if next_N >= len(sequence_fnames):
            sequence_loop.finished = True
        # the Routine "presentation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 50.0 repeats of 'sequence_loop'
    
    
    # --- Prepare to start Routine "fixation" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationComponents = [polygon]
    for thisComponent in fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "fixation" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon.started')
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon.stopped')
                polygon.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fixation" ---
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "recall" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    recall_letter.setText(target)
    recall_movie = visual.MovieStim(
        win=win, name='recall_movie', units='',
        noAudio=True,
        filename=target_fname,
        ori=0.0, pos=(0, 0), opacity=None,
        loop=False, anchor='center',
        size=(0.3,0.5),
        depth=-1.0,
        )
    recall_key.keys = []
    recall_key.rt = []
    _recall_key_allKeys = []
    recall_question.setText(langage['Item presented during the sequence ?'])
    recall_answer.setText(f"{langage['[c]orrect']}                    {langage['[n]ot correct']}")
    # keep track of which components have finished
    recallComponents = [recall_letter, recall_movie, recall_key, recall_question, recall_answer]
    for thisComponent in recallComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "recall" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *recall_letter* updates
        if recall_letter.status == NOT_STARTED and len(target)==1:
            # keep track of start time/frame for later
            recall_letter.frameNStart = frameN  # exact frame index
            recall_letter.tStart = t  # local t and not account for scr refresh
            recall_letter.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recall_letter, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'recall_letter.started')
            recall_letter.setAutoDraw(True)
        
        # *recall_movie* updates
        if recall_movie.status == NOT_STARTED and len(target)>1:
            # keep track of start time/frame for later
            recall_movie.frameNStart = frameN  # exact frame index
            recall_movie.tStart = t  # local t and not account for scr refresh
            recall_movie.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recall_movie, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'recall_movie.started')
            recall_movie.setAutoDraw(True)
            recall_movie.play()
        
        # *recall_key* updates
        waitOnFlip = False
        if recall_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            recall_key.frameNStart = frameN  # exact frame index
            recall_key.tStart = t  # local t and not account for scr refresh
            recall_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recall_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'recall_key.started')
            recall_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(recall_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(recall_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if recall_key.status == STARTED and not waitOnFlip:
            theseKeys = recall_key.getKeys(keyList=['c', 'n'], waitRelease=False)
            _recall_key_allKeys.extend(theseKeys)
            if len(_recall_key_allKeys):
                recall_key.keys = _recall_key_allKeys[-1].name  # just the last key pressed
                recall_key.rt = _recall_key_allKeys[-1].rt
        # Run 'Each Frame' code from end_recall_routine
        if (recall_movie.isFinished or len(target)==1) and len(recall_key.keys)>0:
            continueRoutine = False
        
        # *recall_question* updates
        if recall_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            recall_question.frameNStart = frameN  # exact frame index
            recall_question.tStart = t  # local t and not account for scr refresh
            recall_question.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recall_question, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'recall_question.started')
            recall_question.setAutoDraw(True)
        
        # *recall_answer* updates
        if recall_answer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            recall_answer.frameNStart = frameN  # exact frame index
            recall_answer.tStart = t  # local t and not account for scr refresh
            recall_answer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(recall_answer, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'recall_answer.started')
            recall_answer.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in recallComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "recall" ---
    for thisComponent in recallComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    recall_movie.stop()
    # check responses
    if recall_key.keys in ['', [], None]:  # No response was made
        recall_key.keys = None
    trials.addData('recall_key.keys',recall_key.keys)
    if recall_key.keys != None:  # we had a response
        trials.addData('recall_key.rt', recall_key.rt)
    # the Routine "recall" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "block_questionnaire" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    RSME_labels.reset()
    RSME_ticks.reset()
    RSME_text.setText(f"{langage['Indicate your cognitive effort level by cliking on the scale']}\n\n{langage['Press space to confirm']}")
    RSME_key.keys = []
    RSME_key.rt = []
    _RSME_key_allKeys = []
    # Run 'Begin Routine' code from label_translation
    labels = [langage[label] if label in base_txt else label for label in RSME_labels.labels]
    RSME_labels.labels = labels
    for i, obj in enumerate(RSME_labels.labelObjs):
        # ...set its text to be the corresponding value in labels, and store this in the slider
        obj.text = RSME_labels.labels[i]
    # keep track of which components have finished
    block_questionnaireComponents = [RSME_labels, RSME_ticks, RSME_text, RSME_key]
    for thisComponent in block_questionnaireComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "block_questionnaire" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *RSME_labels* updates
        if RSME_labels.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RSME_labels.frameNStart = frameN  # exact frame index
            RSME_labels.tStart = t  # local t and not account for scr refresh
            RSME_labels.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RSME_labels, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'RSME_labels.started')
            RSME_labels.setAutoDraw(True)
        if RSME_labels.status == STARTED:
            if bool(is_block_ending==False or (RSME_key.rt!=[] and RSME_ticks.rt!=None and RSME_key.rt > RSME_ticks.rt)):
                # keep track of stop time/frame for later
                RSME_labels.tStop = t  # not accounting for scr refresh
                RSME_labels.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RSME_labels.stopped')
                RSME_labels.setAutoDraw(False)
        
        # *RSME_ticks* updates
        if RSME_ticks.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RSME_ticks.frameNStart = frameN  # exact frame index
            RSME_ticks.tStart = t  # local t and not account for scr refresh
            RSME_ticks.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RSME_ticks, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'RSME_ticks.started')
            RSME_ticks.setAutoDraw(True)
        if RSME_ticks.status == STARTED:
            if bool(is_block_ending==False or (RSME_key.rt!=[] and RSME_ticks.rt!=None and RSME_key.rt > RSME_ticks.rt)):
                # keep track of stop time/frame for later
                RSME_ticks.tStop = t  # not accounting for scr refresh
                RSME_ticks.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RSME_ticks.stopped')
                RSME_ticks.setAutoDraw(False)
        
        # *RSME_text* updates
        if RSME_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RSME_text.frameNStart = frameN  # exact frame index
            RSME_text.tStart = t  # local t and not account for scr refresh
            RSME_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RSME_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'RSME_text.started')
            RSME_text.setAutoDraw(True)
        if RSME_text.status == STARTED:
            if bool(is_block_ending==False or (RSME_key.rt!=[] and RSME_ticks.rt!=None and RSME_key.rt > RSME_ticks.rt)):
                # keep track of stop time/frame for later
                RSME_text.tStop = t  # not accounting for scr refresh
                RSME_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RSME_text.stopped')
                RSME_text.setAutoDraw(False)
        
        # *RSME_key* updates
        waitOnFlip = False
        if RSME_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RSME_key.frameNStart = frameN  # exact frame index
            RSME_key.tStart = t  # local t and not account for scr refresh
            RSME_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RSME_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'RSME_key.started')
            RSME_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(RSME_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(RSME_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if RSME_key.status == STARTED:
            if bool(is_block_ending==False or (RSME_key.rt!=[] and RSME_ticks.rt!=None and RSME_key.rt > RSME_ticks.rt)):
                # keep track of stop time/frame for later
                RSME_key.tStop = t  # not accounting for scr refresh
                RSME_key.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RSME_key.stopped')
                RSME_key.status = FINISHED
        if RSME_key.status == STARTED and not waitOnFlip:
            theseKeys = RSME_key.getKeys(keyList=['space'], waitRelease=False)
            _RSME_key_allKeys.extend(theseKeys)
            if len(_RSME_key_allKeys):
                RSME_key.keys = _RSME_key_allKeys[-1].name  # just the last key pressed
                RSME_key.rt = _RSME_key_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block_questionnaireComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "block_questionnaire" ---
    for thisComponent in block_questionnaireComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('RSME_ticks.response', RSME_ticks.getRating())
    trials.addData('RSME_ticks.rt', RSME_ticks.getRT())
    # check responses
    if RSME_key.keys in ['', [], None]:  # No response was made
        RSME_key.keys = None
    trials.addData('RSME_key.keys',RSME_key.keys)
    if RSME_key.keys != None:  # we had a response
        trials.addData('RSME_key.rt', RSME_key.rt)
    # the Routine "block_questionnaire" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
