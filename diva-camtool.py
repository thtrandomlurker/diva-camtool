# MIT License

# Copyright (c) 2020 thatrandomlurker-divamoddingtools

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from math import pi # Grab PI for the deg to rad conversion
from sys import argv # For arguments to define file names

#HUGE credits to minmode, because this script is highly based off his camera base's bone structure
# *and to minmode, if you find this and don't like that i'm using that as a basis to test (even though it doesn't necessarily need you specific diva_camera.pmx
#  i would be more than glad to take this script down

infile = 'cam.csv'
outfile = 'cam.json'




if len(argv) > 1:
    infile = argv[1]
    outfile = argv[2]

if infile[-3] != 'c':
    print('input file not csv, exiting script. if you\'re having issues, then try looking on Google for a program \'VMDConverterGraphical\', it should be the first result.)
    exit()

if outfile[-4] != 'j':
    print('output file name not json. this script outputs a json file for use with PD_Tool, so please name your output file accordingly')
    exit()

out_str = """"""
    
Key_End_Str = """\

            ]
"""

Section_End_Str_Nobreak = """\
          },
"""
    
Section_End_Str = """\
          }
"""
    
base_cam_str = """\
{
  "A3D": {
    "_": {
      "ConverterVersion": "20050823",
"""
base_cam_str_f_name = f"""\
      "FileName": "{outfile[:-4]}a3da",
"""

base_cam_str_prop_ver = """\
      "PropertyVersion": "20050706"
    },
"""

camroot_str = """\
    "CameraRoot": [
      {
        "Interest": {
          "Rot": {
            "X": {
              "Type": "Null"
            },
            "Y": {
              "Type": "Null"
            },
            "Z": {
              "Type": "Null"
            }
          },
          "Scale": {
            "X": {
              "Type": "Value",
              "Value": 1
            },
            "Y": {
              "Type": "Value",
              "Value": 1
            },
            "Z": {
              "Type": "Value",
              "Value": 1
            }
          },
"""

trans_base_str = """\
          "Trans": {
"""

Interest_TransX_base_str = """\
            "X": {
              "Type": "Hermite",
              "Max": 15000,
              "Trans": [
"""

Interest_TransY_base_str = """\
            "Y": {
              "Type": "Hermite",
              "Max": 15000,
              "Trans": [
"""

Interest_TransZ_base_str = """\
            "Z": {
              "Type": "Hermite",
              "Max": 15000,
              "Trans": [
"""

Interest_Visibility_str = """\
          },
          "Visibility": {
            "Type": "Value",
            "Value": 1
          }
        },
"""

ViewPoint_start_str = """\
        "ViewPoint": {
          "Aspect": 1.77778005599976,
          "FOVHorizontal": true,
"""

FOV_start_str = """\
          "FOV": {
            "Type": "Hermite",
            "Max": 15000,
            "Trans": [
"""

FOV_End_str = """\

            ]
          },
"""

Roll_Base_Str = """\
          "Roll": {
            "Type": "Hermite",
            "Max": 15000,
            "Trans": [
"""

ViewPoint_Rotation_Str = """\
          "Rot": {
            "X": {
              "Type": "Null"
            },
            "Y": {
              "Type": "Null"
            },
            "Z": {
              "Type": "Null"
            }
          },
"""

ViewPoint_Unused_Data = """\
          "Scale": {
            "X": {
              "Type": "Value",
              "Value": 1
            },
            "Y": {
              "Type": "Value",
              "Value": 1
            },
            "Z": {
              "Type": "Value",
              "Value": 1
            }
          },
"""

ViewPoint_trans_base_str = """\
          "Trans": {
"""

ViewPoint_TransX_base_str = """\
            "X": {
              "Type": "Hermite",
              "Max": 15000,
              "Trans": [
"""

ViewPoint_TransY_base_str = """\
            "Y": {
              "Type": "Hermite",
              "Max": 15000,
              "Trans": [
"""

ViewPoint_TransZ_base_str = """\
            "Z": {
              "Type": "Hermite",
              "Max": 15000,
              "Trans": [
"""

File_End_Str = """\
          },
          "Visibility": {
            "Type": "Value",
            "Value": 1
          }
        },
        "Rot": {
          "X": {
            "Type": "Null"
          },
          "Y": {
            "Type": "Null"
          },
          "Z": {
            "Type": "Null"
          }
        },
        "Scale": {
          "X": {
            "Type": "Value",
            "Value": 1
          },
          "Y": {
            "Type": "Value",
            "Value": 1
          },
          "Z": {
            "Type": "Value",
            "Value": 1
          }
        },
        "Trans": {
          "X": {
            "Type": "Null"
          },
          "Y": {
            "Type": "Null"
          },
          "Z": {
            "Type": "Null"
          }
        },
        "Visibility": {
          "Type": "Value",
          "Value": 1
        }
      }
    ],
"""

# FPS is 30 because MMD is 30 (unless you use minmode's fork)
# The game supports this though, so there's no real reason to not use it

Play_Control_Str = """\
    "PlayControl": {
      "Begin": 0,
      "FPS": 60,
      "Size": 15000
    }
  }
}
"""

# ok, alot of that was simple, but from here on out, the code turns to spaghetti, since my brain is dying, and i don't know any other way to return the commacounter to 0 from this current code
# so, i just close and reopen the file to reset the loop

# Field of View

with open(infile, 'r', encoding='Shift-JIS') as cam_csv:
    commacounter = 0
    for line in cam_csv:
        datasplit = line.split(',')
        if len(datasplit) >= 3:
            Name = datasplit[0]
            ThirtyFrame = datasplit[1]
            Frame = int(ThirtyFrame) * 2
            MMDTransX = datasplit[2]
            MMDTransY = datasplit[3]
            MMDTransZ = datasplit[4]
            MMDRotX = datasplit[5]
            MMDRotY = datasplit[6]
            MMDRotZ = datasplit[7]
            MMDInterp = datasplit[8]
            
            # FOV Scale
            
            MMDRotXScale = float(MMDRotX) * 2
            
            
            # Radians Conversion
            
            DIVATransX = float(MMDTransX) * pi/180
            DIVATransY = float(MMDTransY) * pi/180
            DIVATransZ = float(MMDTransZ) * pi/180
            DIVARotX = float(MMDRotXScale) * pi/180
            DIVARotY = float(MMDRotY) * pi/180
            DIVARotZ = float(MMDRotZ) * pi/180
            
            if Name == 'fov':
                if commacounter <= 0:
                    FOV_Data_String = f"""\
              [
                {Frame},
                {DIVARotX}
              ]"""
              
                    commacounter += 1
                    
                    FOV_start_str += FOV_Data_String
              
                elif commacounter == 1:
                    FOV_Data_String = f""",
              [
                {Frame},
                {DIVARotX}
              ]"""
              
                    FOV_start_str += FOV_Data_String
              
# Interest X

with open(infile, 'r', encoding='Shift-JIS') as cam_csv:
    commacounter = 0
    for line in cam_csv:
        datasplit = line.split(',')
        if len(datasplit) >= 3:
            Name = datasplit[0]
            ThirtyFrame = datasplit[1]
            Frame = int(ThirtyFrame) * 2
            MMDTransX = datasplit[2]
            MMDTransY = datasplit[3]
            MMDTransZ = datasplit[4]
            MMDRotX = datasplit[5]
            MMDRotY = datasplit[6]
            MMDRotZ = datasplit[7]
            MMDInterp = datasplit[8]
            
            # Scale
            
            MMDTransXScale = float(MMDTransX) * float(5)
            MMDTransYScale = float(MMDTransY) * float(5)
            MMDTransZScale = float(MMDTransZ) * float(5)
            
            # Negative
            
            MMDTransZNeg = float(0) - float(MMDTransZScale)
            
            # Radians Conversion
            
            DIVATransX = float(MMDTransXScale) * pi/180
            DIVATransY = float(MMDTransYScale) * pi/180
            DIVATransZ = float(MMDTransZNeg) * pi/180
            DIVARotX = float(MMDRotX) * pi/180
            DIVARotY = float(MMDRotY) * pi/180
            DIVARotZ = float(MMDRotZ) * pi/180
            
            if Name == 'interest':
                if commacounter <= 0:
                    Interest_X_String = f"""\
              [
                {Frame},
                {DIVATransX}
              ]"""
              
                    commacounter += 1
                    Interest_TransX_base_str += Interest_X_String
              
                elif commacounter == 1:
                    Interest_X_String = f""",
              [
                {Frame},
                {DIVATransX}
              ]"""
              
                    Interest_TransX_base_str += Interest_X_String
                    
# Interest Y

with open(infile, 'r', encoding='Shift-JIS') as cam_csv:
    commacounter = 0
    for line in cam_csv:
        datasplit = line.split(',')
        if len(datasplit) >= 3:
            Name = datasplit[0]
            ThirtyFrame = datasplit[1]
            Frame = int(ThirtyFrame) * 2
            MMDTransX = datasplit[2]
            MMDTransY = datasplit[3]
            MMDTransZ = datasplit[4]
            MMDRotX = datasplit[5]
            MMDRotY = datasplit[6]
            MMDRotZ = datasplit[7]
            MMDInterp = datasplit[8]
            
            # Scale
            
            MMDTransXScale = float(MMDTransX) * float(4.57971014493)
            MMDTransYScale = float(MMDTransY) * float(4.57971014493)
            MMDTransZScale = float(MMDTransZ) * float(4.57971014493)
            
            # Negative
            
            MMDTransZNeg = float(0) - float(MMDTransZScale)
            
            # Radians Conversion
            
            DIVATransX = float(MMDTransXScale) * pi/180
            DIVATransY = float(MMDTransYScale) * pi/180
            DIVATransZ = float(MMDTransZNeg) * pi/180
            DIVARotX = float(MMDRotX) * pi/180
            DIVARotY = float(MMDRotY) * pi/180
            DIVARotZ = float(MMDRotZ) * pi/180
            
            if Name == 'interest':
                if commacounter <= 0:
                    Interest_Y_String = f"""\
              [
                {Frame},
                {DIVATransY}
              ]"""
              
                    commacounter += 1
                    Interest_TransY_base_str += Interest_Y_String
              
                elif commacounter == 1:
                    Interest_Y_String = f""",
              [
                {Frame},
                {DIVATransY}
              ]"""
              
                    Interest_TransY_base_str += Interest_Y_String
                    
# Interest Z

with open(infile, 'r', encoding='Shift-JIS') as cam_csv:
    commacounter = 0
    for line in cam_csv:
        datasplit = line.split(',')
        if len(datasplit) >= 3:
            Name = datasplit[0]
            ThirtyFrame = datasplit[1]
            Frame = int(ThirtyFrame) * 2
            MMDTransX = datasplit[2]
            MMDTransY = datasplit[3]
            MMDTransZ = datasplit[4]
            MMDRotX = datasplit[5]
            MMDRotY = datasplit[6]
            MMDRotZ = datasplit[7]
            MMDInterp = datasplit[8]
            
            # Scale
            
            MMDTransXScale = float(MMDTransX) * float(4.57971014493)
            MMDTransYScale = float(MMDTransY) * float(4.57971014493)
            MMDTransZScale = float(MMDTransZ) * float(4.57971014493)
            
            # Negative
            
            MMDTransZNeg = float(0) - float(MMDTransZScale)
            
            # Radians Conversion
            
            DIVATransX = float(MMDTransXScale) * pi/180
            DIVATransY = float(MMDTransYScale) * pi/180
            DIVATransZ = float(MMDTransZNeg) * pi/180
            DIVARotX = float(MMDRotX) * pi/180
            DIVARotY = float(MMDRotY) * pi/180
            DIVARotZ = float(MMDRotZ) * pi/180
            
            if Name == 'interest':
                if commacounter <= 0:
                    Interest_Z_String = f"""\
              [
                {Frame},
                {DIVATransZ}
              ]"""
              
                    commacounter += 1
                    Interest_TransZ_base_str += Interest_Z_String
              
                elif commacounter == 1:
                    Interest_Z_String = f""",
              [
                {Frame},
                {DIVATransZ}
              ]"""
              
                    Interest_TransZ_base_str += Interest_Z_String
                    
# ViewPoint X

with open(infile, 'r', encoding='Shift-JIS') as cam_csv:
    commacounter = 0
    for line in cam_csv:
        datasplit = line.split(',')
        if len(datasplit) >= 3:
            Name = datasplit[0]
            ThirtyFrame = datasplit[1]
            Frame = int(ThirtyFrame) * 2
            MMDTransX = datasplit[2]
            MMDTransY = datasplit[3]
            MMDTransZ = datasplit[4]
            MMDRotX = datasplit[5]
            MMDRotY = datasplit[6]
            MMDRotZ = datasplit[7]
            MMDInterp = datasplit[8]
            
            # Scale
            
            MMDTransXScale = float(MMDTransX) * float(4.57971014493)
            MMDTransYScale = float(MMDTransY) * float(4.57971014493)
            MMDTransZScale = float(MMDTransZ) * float(4.57971014493)
            
            # Negative
            
            MMDTransZNeg = float(0) - float(MMDTransZScale)
            
            # Radians Conversion
            
            DIVATransX = float(MMDTransXScale) * pi/180
            DIVATransY = float(MMDTransYScale) * pi/180
            DIVATransZ = float(MMDTransZNeg) * pi/180
            DIVARotX = float(MMDRotX) * pi/180
            DIVARotY = float(MMDRotY) * pi/180
            DIVARotZ = float(MMDRotZ) * pi/180
            
            if Name == 'view_point':
                if commacounter <= 0:
                    ViewPoint_X_String = f"""\
              [
                {Frame},
                {DIVATransX}
              ]"""
              
                    commacounter += 1
                    ViewPoint_TransX_base_str += ViewPoint_X_String
              
                elif commacounter == 1:
                    ViewPoint_X_String = f""",
              [
                {Frame},
                {DIVATransX}
              ]"""
              
                    ViewPoint_TransX_base_str += ViewPoint_X_String
                    
# ViewPoint Y

with open(infile, 'r', encoding='Shift-JIS') as cam_csv:
    commacounter = 0
    for line in cam_csv:
        datasplit = line.split(',')
        if len(datasplit) >= 3:
            Name = datasplit[0]
            ThirtyFrame = datasplit[1]
            Frame = int(ThirtyFrame) * 2
            MMDTransX = datasplit[2]
            MMDTransY = datasplit[3]
            MMDTransZ = datasplit[4]
            MMDRotX = datasplit[5]
            MMDRotY = datasplit[6]
            MMDRotZ = datasplit[7]
            MMDInterp = datasplit[8]
            
            # Scale
            
            MMDTransXScale = float(MMDTransX) * float(4.57971014493)
            MMDTransYScale = float(MMDTransY) * float(4.57971014493)
            MMDTransZScale = float(MMDTransZ) * float(4.57971014493)
            
            # Negative
            
            MMDTransZNeg = float(0) - float(MMDTransZScale)
            
            # Radians Conversion
            
            DIVATransX = float(MMDTransXScale) * pi/180
            DIVATransY = float(MMDTransYScale) * pi/180
            DIVATransZ = float(MMDTransZNeg) * pi/180
            DIVARotX = float(MMDRotX) * pi/180
            DIVARotY = float(MMDRotY) * pi/180
            DIVARotZ = float(MMDRotZ) * pi/180
            
            if Name == 'view_point':
                if commacounter <= 0:
                    ViewPoint_Y_String = f"""\
              [
                {Frame},
                {DIVATransY}
              ]"""
              
                    commacounter += 1
                    ViewPoint_TransY_base_str += ViewPoint_Y_String
              
                elif commacounter == 1:
                    ViewPoint_Y_String = f""",
              [
                {Frame},
                {DIVATransY}
              ]"""
              
                    ViewPoint_TransY_base_str += ViewPoint_Y_String
                    
# ViewPoint Z

with open(infile, 'r', encoding='Shift-JIS') as cam_csv:
    commacounter = 0
    for line in cam_csv:
        datasplit = line.split(',')
        if len(datasplit) >= 3:
            Name = datasplit[0]
            ThirtyFrame = datasplit[1]
            Frame = int(ThirtyFrame) * 2
            MMDTransX = datasplit[2]
            MMDTransY = datasplit[3]
            MMDTransZ = datasplit[4]
            MMDRotX = datasplit[5]
            MMDRotY = datasplit[6]
            MMDRotZ = datasplit[7]
            MMDInterp = datasplit[8]
            
            # Scale
            
            MMDTransXScale = float(MMDTransX) * float(4.57971014493)
            MMDTransYScale = float(MMDTransY) * float(4.57971014493)
            MMDTransZScale = float(MMDTransZ) * float(4.57971014493)
            
            # Negative
            
            MMDTransZNeg = float(0) - float(MMDTransZScale)
            
            # Radians Conversion
            
            DIVATransX = float(MMDTransXScale) * pi/180
            DIVATransY = float(MMDTransYScale) * pi/180
            DIVATransZ = float(MMDTransZNeg) * pi/180
            DIVARotX = float(MMDRotX) * pi/180
            DIVARotY = float(MMDRotY) * pi/180
            DIVARotZ = float(MMDRotZ) * pi/180
            
            if Name == 'view_point':
                if commacounter <= 0:
                    ViewPoint_Z_String = f"""\
              [
                {Frame},
                {DIVATransZ}
              ]"""
              
                    commacounter += 1
                    ViewPoint_TransZ_base_str += ViewPoint_Z_String
              
                elif commacounter == 1:
                    ViewPoint_Z_String = f""",
              [
                {Frame},
                {DIVATransZ}
              ]"""
              
                    ViewPoint_TransZ_base_str += ViewPoint_Z_String
                    
# Rotation Z

with open(infile, 'r', encoding='Shift-JIS') as cam_csv:
    commacounter = 0
    for line in cam_csv:
        datasplit = line.split(',')
        if len(datasplit) >= 3:
            Name = datasplit[0]
            ThirtyFrame = datasplit[1]
            Frame = int(ThirtyFrame) * 2
            MMDTransX = datasplit[2]
            MMDTransY = datasplit[3]
            MMDTransZ = datasplit[4]
            MMDRotX = datasplit[5]
            MMDRotY = datasplit[6]
            MMDRotZ = datasplit[7]
            MMDInterp = datasplit[8]
            
            # Scale
            
            MMDTransXScale = float(MMDTransX) * float(4.57971014493)
            MMDTransYScale = float(MMDTransY) * float(4.57971014493)
            MMDTransZScale = float(MMDTransZ) * float(4.57971014493)
            
            # Invert the rotation
            
            MMDRotZNeg = float(MMDRotZ) - float(180)
            
            # Radians Conversion
            
            DIVATransX = float(MMDTransXScale) * pi/180
            DIVATransY = float(MMDTransYScale) * pi/180
            DIVATransZ = float(MMDTransZNeg) * pi/180
            DIVARotX = float(MMDRotX) * pi/180
            DIVARotY = float(MMDRotY) * pi/180
            DIVARotZ = float(MMDRotZNeg) * pi/180
            
            if Name == 'view_point':
                if commacounter <= 0:
                    ViewPoint_Roll_Value_Str = f"""\
              [
                {Frame},
                {DIVARotZ}
              ]"""
              
                    commacounter += 1
                    Roll_Base_Str += ViewPoint_Roll_Value_Str
              
                elif commacounter == 1:
                    ViewPoint_Roll_Value_Str = f""",
              [
                {Frame},
                {DIVARotZ}
              ]"""
              
                    Roll_Base_Str += ViewPoint_Roll_Value_Str

# all right, time to shove the file together (wish me luck)

out_str += base_cam_str
out_str += base_cam_str_f_name
out_str += base_cam_str_prop_ver
out_str += camroot_str
out_str += trans_base_str # Interest
out_str += Interest_TransX_base_str
out_str += Key_End_Str
out_str += Section_End_Str_Nobreak
out_str += Interest_TransY_base_str
out_str += Key_End_Str
out_str += Section_End_Str_Nobreak
out_str += Interest_TransZ_base_str
out_str += Key_End_Str
out_str += Section_End_Str
out_str += Interest_Visibility_str
out_str += ViewPoint_start_str
out_str += FOV_start_str
out_str += FOV_End_str
out_str += Roll_Base_Str
out_str += Key_End_Str
out_str += Section_End_Str_Nobreak
out_str += ViewPoint_Rotation_Str
out_str += ViewPoint_Unused_Data
out_str += ViewPoint_trans_base_str
out_str += ViewPoint_TransX_base_str
out_str += Key_End_Str
out_str += Section_End_Str_Nobreak
out_str += ViewPoint_TransY_base_str
out_str += Key_End_Str
out_str += Section_End_Str_Nobreak
out_str += ViewPoint_TransZ_base_str
out_str += Key_End_Str
out_str += Section_End_Str
out_str += File_End_Str
out_str += Play_Control_Str

with open(outfile, 'w') as diva_cam:
    diva_cam.write(out_str)
    
print("successfully wrote cam JSON, please note this tool is in beta, and the output may not work as expected")

# Tool written by ThatRandomLurker, A3DA Json layout by KorenKonder
