#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Peidong
"""
import os

########################################################
#
# print('Part A')
#
# file_location = str(os.getcwd()) + '/A_StressAroundCrack'
#
# os.system('python ' + file_location +'/'+ 'A_StressAroundCrack_1fig_2by2.py')

########################################################

# print('Part B')
#
# file_location = str(os.getcwd()) + '/B_SlipZone_3'
#
# os.system('python ' + file_location +'/'+ 'B_SlipZone_3_Criteria_90.py')

#########################################################

print('Part C')

file_location = str(os.getcwd()) + '/' + 'C_SlipZoneArea'

os.system('python ' + file_location +'/'+ 'B_SlipZone_Effect_Beta.py')
os.system('python ' + file_location +'/'+ 'C_SlipZoneArea_01_StressDiff.py')
os.system('python ' + file_location +'/'+ 'C_SlipZoneArea_02_ConfineStress.py')
os.system('python ' + file_location +'/'+ 'C_SlipZoneArea_03_P_Net.py')
os.system('python ' + file_location +'/'+ 'C_SlipZoneArea_04_OverPressure.py')
os.system('python ' + file_location +'/'+ 'C_SlipZoneArea_05_miu.py')
os.system('python ' + file_location +'/'+ 'C_SlipZoneArea_06_Length.py')