
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AMBIENT BASENAME BOX CAMERA CO COMMENT CONSTANTS CYLINDER DISPLAY DOUBLE FOCAL FRAMES GENERATE_RAYFILES HOLLOW_CYLINDER ID INT LIGHT LINE MESH MOVE POP PUSH ROTATE SAVE SAVE_COORDS SAVE_KNOBS SCALE SCREEN SET SET_KNOBS SHADING SHADING_TYPE SPHERE STRING TEXTURE TORUS TWEEN VARY WEB XYZinput :\n            | command inputcommand : COMMENTSYMBOL : XYZ\n              | IDTEXT : SYMBOL\n            | STRINGNUMBER : DOUBLEcommand : POP\n                 | PUSHcommand : SCREEN NUMBER NUMBER\n                 | SCREENcommand : SAVE TEXT TEXTcommand : DISPLAYcommand : CYLINDER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | CYLINDER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | CYLINDER SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER\n               | CYLINDER SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOLcommand : HOLLOW_CYLINDER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | HOLLOW_CYLINDER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | HOLLOW_CYLINDER SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | HOLLOW_CYLINDER SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOLcommand : SPHERE NUMBER NUMBER NUMBER NUMBER\n               | SPHERE SYMBOL NUMBER NUMBER NUMBER NUMBER\n               | SPHERE NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | SPHERE SYMBOL NUMBER NUMBER NUMBER NUMBER SYMBOLcommand : TORUS NUMBER NUMBER NUMBER NUMBER NUMBER\n               | TORUS NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | TORUS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER\n               | TORUS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOLcommand : BOX NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | BOX NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | BOX SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | BOX SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOLcommand : LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER\n               | LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOL\n               | LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER\n               | LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOLcommand : MOVE NUMBER NUMBER NUMBER SYMBOL\n               | MOVE NUMBER NUMBER NUMBERcommand : SCALE NUMBER NUMBER NUMBER SYMBOL\n                 | SCALE NUMBER NUMBER NUMBERcommand : ROTATE XYZ NUMBER SYMBOL\n                 | ROTATE XYZ NUMBERcommand : FRAMES NUMBERcommand : BASENAME TEXTcommand : VARY SYMBOL NUMBER NUMBER NUMBER NUMBERcommand : SET SYMBOL NUMBER\n               | SET_KNOBS NUMBERcommand : AMBIENT NUMBER NUMBER NUMBERcommand : CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBERcommand : LIGHT SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBERcommand : SHADING SHADING_TYPEcommand : CAMERA NUMBER NUMBER NUMBER NUMBER NUMBER NUMBERcommand : GENERATE_RAYFILEScommand : MESH CO TEXT\n               | MESH SYMBOL CO TEXT\n               | MESH CO TEXT SYMBOL\n               | MESH SYMBOL CO TEXT SYMBOLcommand : SAVE_KNOBS SYMBOLcommand : SAVE_COORDS SYMBOLcommand : TWEEN NUMBER NUMBER SYMBOL SYMBOLcommand : FOCAL NUMBERcommand : WEBcommand : TEXTURE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER'
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,8,28,34,36,38,40,41,42,43,59,60,63,67,71,72,74,76,77,92,94,99,115,116,117,119,123,124,131,140,141,146,147,149,153,154,155,163,168,169,170,172,173,174,175,177,183,185,186,187,188,189,190,191,192,194,196,198,199,200,201,202,205,208,214,215,],[-1,0,-1,-3,-9,-10,-12,-14,-60,-69,-2,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-23,-43,-45,-64,-67,-15,-25,-24,-27,-51,-16,-17,-19,-26,-28,-29,-31,-35,-59,-18,-20,-21,-30,-32,-33,-36,-37,-39,-57,-22,-34,-38,-41,-40,-42,-55,-56,-70,]),'COMMENT':([0,2,3,4,5,6,8,28,34,38,40,41,42,43,59,60,63,67,71,72,74,76,77,92,94,99,115,116,117,119,123,124,131,140,141,146,147,149,153,154,155,163,168,169,170,172,173,174,175,177,183,185,186,187,188,189,190,191,192,194,196,198,199,200,201,202,205,208,214,215,],[3,3,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-23,-43,-45,-64,-67,-15,-25,-24,-27,-51,-16,-17,-19,-26,-28,-29,-31,-35,-59,-18,-20,-21,-30,-32,-33,-36,-37,-39,-57,-22,-34,-38,-41,-40,-42,-55,-56,-70,]),'POP':([0,2,3,4,5,6,8,28,34,38,40,41,42,43,59,60,63,67,71,72,74,76,77,92,94,99,115,116,117,119,123,124,131,140,141,146,147,149,153,154,155,163,168,169,170,172,173,174,175,177,183,185,186,187,188,189,190,191,192,194,196,198,199,200,201,202,205,208,214,215,],[4,4,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-23,-43,-45,-64,-67,-15,-25,-24,-27,-51,-16,-17,-19,-26,-28,-29,-31,-35,-59,-18,-20,-21,-30,-32,-33,-36,-37,-39,-57,-22,-34,-38,-41,-40,-42,-55,-56,-70,]),'PUSH':([0,2,3,4,5,6,8,28,34,38,40,41,42,43,59,60,63,67,71,72,74,76,77,92,94,99,115,116,117,119,123,124,131,140,141,146,147,149,153,154,155,163,168,169,170,172,173,174,175,177,183,185,186,187,188,189,190,191,192,194,196,198,199,200,201,202,205,208,214,215,],[5,5,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-23,-43,-45,-64,-67,-15,-25,-24,-27,-51,-16,-17,-19,-26,-28,-29,-31,-35,-59,-18,-20,-21,-30,-32,-33,-36,-37,-39,-57,-22,-34,-38,-41,-40,-42,-55,-56,-70,]),'SCREEN':([0,2,3,4,5,6,8,28,34,38,40,41,42,43,59,60,63,67,71,72,74,76,77,92,94,99,115,116,117,119,123,124,131,140,141,146,147,149,153,154,155,163,168,169,170,172,173,174,175,177,183,185,186,187,188,189,190,191,192,194,196,198,199,200,201,202,205,208,214,215,],[6,6,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-23,-43,-45,-64,-67,-15,-25,-24,-27,-51,-16,-17,-19,-26,-28,-29,-31,-35,-59,-18,-20,-21,-30,-32,-33,-36,-37,-39,-57,-22,-34,-38,-41,-40,-42,-55,-56,-70,]),'SAVE':([0,2,3,4,5,6,8,28,34,38,40,41,42,43,59,60,63,67,71,72,74,76,77,92,94,99,115,116,117,119,123,124,131,140,141,146,147,149,153,154,155,163,168,169,170,172,173,174,175,177,183,185,186,187,188,189,190,191,192,194,196,198,199,200,201,202,205,208,214,215,],[7,7,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-23,-43,-45,-64,-67,-15,-25,-24,-27,-51,-16,-17,-19,-26,-28,-29,-31,-35,-59,-18,-20,-21,-30,-32,-33,-36,-37,-39,-57,-22,-34,-38,-41,-40,-42,-55,-56,-70,]),'DISPLAY':([0,2,3,4,5,6,8,28,34,38,40,41,42,43,59,60,63,67,71,72,74,76,77,92,94,99,115,116,117,119,123,124,131,140,141,146,147,149,153,154,155,163,168,169,170,172,173,174,175,177,183,185,186,187,188,189,190,191,192,194,196,198,199,200,201,202,205,208,214,215,],[8,8,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-23,-43,-45,-64,-67,-15,-25,-24,-27,-51,-16,-17,-19,-26,-28,-29,-31,-35,-59,-18,-20,-21,-30,-32,-33,-36,-37,-39,-57,-22,-34,-38,-41,-40,-42,-55,-56,-70,]),'CYLINDER':([0,2,3,4,5,6,8,28,34,38,40,41,42,43,59,60,63,67,71,72,74,76,77,92,94,99,115,116,117,119,123,124,131,140,141,146,147,149,153,154,155,163,168,169,170,172,173,174,175,177,183,185,186,187,188,189,190,191,192,194,196,198,199,200,201,202,205,208,214,215,],[9,9,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-23,-43,-45,-64,-67,-15,-25,-24,-27,-51,-16,-17,-19,-26,-28,-29,-31,-35,-59,-18,-20,-21,-30,-32,-33,-36,-37,-39,-57,-22,-34,-38,-41,-40,-42,-55,-56,-70,]),'HOLLOW_CYLINDER':([0,2,3,4,5,6,8,28,34,38,40,41,42,43,59,60,63,67,71,72,74,76,77,92,94,99,115,116,117,119,123,124,131,140,141,146,147,149,153,154,155,163,168,169,170,172,173,174,175,177,183,185,186,187,188,189,190,191,192,194,196,198,199,200,201,202,205,208,214,215,],[10,10,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-23,-43,-45,-64,-67,-15,-25,-24,-27,-51,-16,-17,-19,-26,-28,-29,-31,-35,-59,-18,-20,-21,-30,-32,-33,-36,-37,-39,-57,-22,-34,-38,-41,-40,-42,-55,-56,-70,]),'SPHERE':([0,2,3,4,5,6,8,28,34,38,40,41,42,43,59,60,63,67,71,72,74,76,77,92,94,99,115,116,117,119,123,124,131,140,141,146,147,149,153,154,155,163,168,169,170,172,173,174,175,177,183,185,186,187,188,189,190,191,192,194,196,198,199,200,201,202,205,208,214,215,],[11,11,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-23,-43,-45,-64,-67,-15,-25,-24,-27,-51,-16,-17,-19,-26,-28,-29,-31,-35,-59,-18,-20,-21,-30,-32,-33,-36,-37,-39,-57,-22,-34,-38,-41,-40,-42,-55,-56,-70,]),'TORUS':([0,2,3,4,5,6,8,28,34,38,40,41,42,43,59,60,63,67,71,72,74,76,77,92,94,99,115,116,117,119,123,124,131,140,141,146,147,149,153,154,155,163,168,169,170,172,173,174,175,177,183,185,186,187,188,189,190,191,192,194,196,198,199,200,201,202,205,208,214,215,],[12,12,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-23,-43,-45,-64,-67,-15,-25,-24,-27,-51,-16,-17,-19,-26,-28,-29,-31,-35,-59,-18,-20,-21,-30,-32,-33,-36,-37,-39,-57,-22,-34,-38,-41,-40,-42,-55,-56,-70,]),'BOX':([0,2,3,4,5,6,8,28,34,38,40,41,42,43,59,60,63,67,71,72,74,76,77,92,94,99,115,116,117,119,123,124,131,140,141,146,147,149,153,154,155,163,168,169,170,172,173,174,175,177,183,185,186,187,188,189,190,191,192,194,196,198,199,200,201,202,205,208,214,215,],[13,13,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-23,-43,-45,-64,-67,-15,-25,-24,-27,-51,-16,-17,-19,-26,-28,-29,-31,-35,-59,-18,-20,-21,-30,-32,-33,-36,-37,-39,-57,-22,-34,-38,-41,-40,-42,-55,-56,-70,]),'LINE':([0,2,3,4,5,6,8,28,34,38,40,41,42,43,59,60,63,67,71,72,74,76,77,92,94,99,115,116,117,119,123,124,131,140,141,146,147,149,153,154,155,163,168,169,170,172,173,174,175,177,183,185,186,187,188,189,190,191,192,194,196,198,199,200,201,202,205,208,214,215,],[14,14,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-23,-43,-45,-64,-67,-15,-25,-24,-27,-51,-16,-17,-19,-26,-28,-29,-31,-35,-59,-18,-20,-21,-30,-32,-33,-36,-37,-39,-57,-22,-34,-38,-41,-40,-42,-55,-56,-70,]),'MOVE':([0,2,3,4,5,6,8,28,34,38,40,41,42,43,59,60,63,67,71,72,74,76,77,92,94,99,115,116,117,119,123,124,131,140,141,146,147,149,153,154,155,163,168,169,170,172,173,174,175,177,183,185,186,187,188,189,190,191,192,194,196,198,199,200,201,202,205,208,214,215,],[15,15,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-23,-43,-45,-64,-67,-15,-25,-24,-27,-51,-16,-17,-19,-26,-28,-29,-31,-35,-59,-18,-20,-21,-30,-32,-33,-36,-37,-39,-57,-22,-34,-38,-41,-40,-42,-55,-56,-70,]),'SCALE':([0,2,3,4,5,6,8,28,34,38,40,41,42,43,59,60,63,67,71,72,74,76,77,92,94,99,115,116,117,119,123,124,131,140,141,146,147,149,153,154,155,163,168,169,170,172,173,174,175,177,183,185,186,187,188,189,190,191,192,194,196,198,199,200,201,202,205,208,214,215,],[16,16,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-23,-43,-45,-64,-67,-15,-25,-24,-27,-51,-16,-17,-19,-26,-28,-29,-31,-35,-59,-18,-20,-21,-30,-32,-33,-36,-37,-39,-57,-22,-34,-38,-41,-40,-42,-55,-56,-70,]),'ROTATE':([0,2,3,4,5,6,8,28,34,38,40,41,42,43,59,60,63,67,71,72,74,76,77,92,94,99,115,116,117,119,123,124,131,140,141,146,147,149,153,154,155,163,168,169,170,172,173,174,175,177,183,185,186,187,188,189,190,191,192,194,196,198,199,200,201,202,205,208,214,215,],[17,17,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-23,-43,-45,-64,-67,-15,-25,-24,-27,-51,-16,-17,-19,-26,-28,-29,-31,-35,-59,-18,-20,-21,-30,-32,-33,-36,-37,-39,-57,-22,-34,-38,-41,-40,-42,-55,-56,-70,]),'FRAMES':([0,2,3,4,5,6,8,28,34,38,40,41,42,43,59,60,63,67,71,72,74,76,77,92,94,99,115,116,117,119,123,124,131,140,141,146,147,149,153,154,155,163,168,169,170,172,173,174,175,177,183,185,186,187,188,189,190,191,192,194,196,198,199,200,201,202,205,208,214,215,],[18,18,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-23,-43,-45,-64,-67,-15,-25,-24,-27,-51,-16,-17,-19,-26,-28,-29,-31,-35,-59,-18,-20,-21,-30,-32,-33,-36,-37,-39,-57,-22,-34,-38,-41,-40,-42,-55,-56,-70,]),'BASENAME':([0,2,3,4,5,6,8,28,34,38,40,41,42,43,59,60,63,67,71,72,74,76,77,92,94,99,115,116,117,119,123,124,131,140,141,146,147,149,153,154,155,163,168,169,170,172,173,174,175,177,183,185,186,187,188,189,190,191,192,194,196,198,199,200,201,202,205,208,214,215,],[19,19,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-23,-43,-45,-64,-67,-15,-25,-24,-27,-51,-16,-17,-19,-26,-28,-29,-31,-35,-59,-18,-20,-21,-30,-32,-33,-36,-37,-39,-57,-22,-34,-38,-41,-40,-42,-55,-56,-70,]),'VARY':([0,2,3,4,5,6,8,28,34,38,40,41,42,43,59,60,63,67,71,72,74,76,77,92,94,99,115,116,117,119,123,124,131,140,141,146,147,149,153,154,155,163,168,169,170,172,173,174,175,177,183,185,186,187,188,189,190,191,192,194,196,198,199,200,201,202,205,208,214,215,],[20,20,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-23,-43,-45,-64,-67,-15,-25,-24,-27,-51,-16,-17,-19,-26,-28,-29,-31,-35,-59,-18,-20,-21,-30,-32,-33,-36,-37,-39,-57,-22,-34,-38,-41,-40,-42,-55,-56,-70,]),'SET':([0,2,3,4,5,6,8,28,34,38,40,41,42,43,59,60,63,67,71,72,74,76,77,92,94,99,115,116,117,119,123,124,131,140,141,146,147,149,153,154,155,163,168,169,170,172,173,174,175,177,183,185,186,187,188,189,190,191,192,194,196,198,199,200,201,202,205,208,214,215,],[21,21,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-23,-43,-45,-64,-67,-15,-25,-24,-27,-51,-16,-17,-19,-26,-28,-29,-31,-35,-59,-18,-20,-21,-30,-32,-33,-36,-37,-39,-57,-22,-34,-38,-41,-40,-42,-55,-56,-70,]),'SET_KNOBS':([0,2,3,4,5,6,8,28,34,38,40,41,42,43,59,60,63,67,71,72,74,76,77,92,94,99,115,116,117,119,123,124,131,140,141,146,147,149,153,154,155,163,168,169,170,172,173,174,175,177,183,185,186,187,188,189,190,191,192,194,196,198,199,200,201,202,205,208,214,215,],[22,22,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-23,-43,-45,-64,-67,-15,-25,-24,-27,-51,-16,-17,-19,-26,-28,-29,-31,-35,-59,-18,-20,-21,-30,-32,-33,-36,-37,-39,-57,-22,-34,-38,-41,-40,-42,-55,-56,-70,]),'AMBIENT':([0,2,3,4,5,6,8,28,34,38,40,41,42,43,59,60,63,67,71,72,74,76,77,92,94,99,115,116,117,119,123,124,131,140,141,146,147,149,153,154,155,163,168,169,170,172,173,174,175,177,183,185,186,187,188,189,190,191,192,194,196,198,199,200,201,202,205,208,214,215,],[23,23,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-23,-43,-45,-64,-67,-15,-25,-24,-27,-51,-16,-17,-19,-26,-28,-29,-31,-35,-59,-18,-20,-21,-30,-32,-33,-36,-37,-39,-57,-22,-34,-38,-41,-40,-42,-55,-56,-70,]),'CONSTANTS':([0,2,3,4,5,6,8,28,34,38,40,41,42,43,59,60,63,67,71,72,74,76,77,92,94,99,115,116,117,119,123,124,131,140,141,146,147,149,153,154,155,163,168,169,170,172,173,174,175,177,183,185,186,187,188,189,190,191,192,194,196,198,199,200,201,202,205,208,214,215,],[24,24,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-23,-43,-45,-64,-67,-15,-25,-24,-27,-51,-16,-17,-19,-26,-28,-29,-31,-35,-59,-18,-20,-21,-30,-32,-33,-36,-37,-39,-57,-22,-34,-38,-41,-40,-42,-55,-56,-70,]),'LIGHT':([0,2,3,4,5,6,8,28,34,38,40,41,42,43,59,60,63,67,71,72,74,76,77,92,94,99,115,116,117,119,123,124,131,140,141,146,147,149,153,154,155,163,168,169,170,172,173,174,175,177,183,185,186,187,188,189,190,191,192,194,196,198,199,200,201,202,205,208,214,215,],[25,25,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-23,-43,-45,-64,-67,-15,-25,-24,-27,-51,-16,-17,-19,-26,-28,-29,-31,-35,-59,-18,-20,-21,-30,-32,-33,-36,-37,-39,-57,-22,-34,-38,-41,-40,-42,-55,-56,-70,]),'SHADING':([0,2,3,4,5,6,8,28,34,38,40,41,42,43,59,60,63,67,71,72,74,76,77,92,94,99,115,116,117,119,123,124,131,140,141,146,147,149,153,154,155,163,168,169,170,172,173,174,175,177,183,185,186,187,188,189,190,191,192,194,196,198,199,200,201,202,205,208,214,215,],[26,26,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-23,-43,-45,-64,-67,-15,-25,-24,-27,-51,-16,-17,-19,-26,-28,-29,-31,-35,-59,-18,-20,-21,-30,-32,-33,-36,-37,-39,-57,-22,-34,-38,-41,-40,-42,-55,-56,-70,]),'CAMERA':([0,2,3,4,5,6,8,28,34,38,40,41,42,43,59,60,63,67,71,72,74,76,77,92,94,99,115,116,117,119,123,124,131,140,141,146,147,149,153,154,155,163,168,169,170,172,173,174,175,177,183,185,186,187,188,189,190,191,192,194,196,198,199,200,201,202,205,208,214,215,],[27,27,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-23,-43,-45,-64,-67,-15,-25,-24,-27,-51,-16,-17,-19,-26,-28,-29,-31,-35,-59,-18,-20,-21,-30,-32,-33,-36,-37,-39,-57,-22,-34,-38,-41,-40,-42,-55,-56,-70,]),'GENERATE_RAYFILES':([0,2,3,4,5,6,8,28,34,38,40,41,42,43,59,60,63,67,71,72,74,76,77,92,94,99,115,116,117,119,123,124,131,140,141,146,147,149,153,154,155,163,168,169,170,172,173,174,175,177,183,185,186,187,188,189,190,191,192,194,196,198,199,200,201,202,205,208,214,215,],[28,28,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-23,-43,-45,-64,-67,-15,-25,-24,-27,-51,-16,-17,-19,-26,-28,-29,-31,-35,-59,-18,-20,-21,-30,-32,-33,-36,-37,-39,-57,-22,-34,-38,-41,-40,-42,-55,-56,-70,]),'MESH':([0,2,3,4,5,6,8,28,34,38,40,41,42,43,59,60,63,67,71,72,74,76,77,92,94,99,115,116,117,119,123,124,131,140,141,146,147,149,153,154,155,163,168,169,170,172,173,174,175,177,183,185,186,187,188,189,190,191,192,194,196,198,199,200,201,202,205,208,214,215,],[29,29,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-23,-43,-45,-64,-67,-15,-25,-24,-27,-51,-16,-17,-19,-26,-28,-29,-31,-35,-59,-18,-20,-21,-30,-32,-33,-36,-37,-39,-57,-22,-34,-38,-41,-40,-42,-55,-56,-70,]),'SAVE_KNOBS':([0,2,3,4,5,6,8,28,34,38,40,41,42,43,59,60,63,67,71,72,74,76,77,92,94,99,115,116,117,119,123,124,131,140,141,146,147,149,153,154,155,163,168,169,170,172,173,174,175,177,183,185,186,187,188,189,190,191,192,194,196,198,199,200,201,202,205,208,214,215,],[30,30,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-23,-43,-45,-64,-67,-15,-25,-24,-27,-51,-16,-17,-19,-26,-28,-29,-31,-35,-59,-18,-20,-21,-30,-32,-33,-36,-37,-39,-57,-22,-34,-38,-41,-40,-42,-55,-56,-70,]),'SAVE_COORDS':([0,2,3,4,5,6,8,28,34,38,40,41,42,43,59,60,63,67,71,72,74,76,77,92,94,99,115,116,117,119,123,124,131,140,141,146,147,149,153,154,155,163,168,169,170,172,173,174,175,177,183,185,186,187,188,189,190,191,192,194,196,198,199,200,201,202,205,208,214,215,],[31,31,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-23,-43,-45,-64,-67,-15,-25,-24,-27,-51,-16,-17,-19,-26,-28,-29,-31,-35,-59,-18,-20,-21,-30,-32,-33,-36,-37,-39,-57,-22,-34,-38,-41,-40,-42,-55,-56,-70,]),'TWEEN':([0,2,3,4,5,6,8,28,34,38,40,41,42,43,59,60,63,67,71,72,74,76,77,92,94,99,115,116,117,119,123,124,131,140,141,146,147,149,153,154,155,163,168,169,170,172,173,174,175,177,183,185,186,187,188,189,190,191,192,194,196,198,199,200,201,202,205,208,214,215,],[32,32,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-23,-43,-45,-64,-67,-15,-25,-24,-27,-51,-16,-17,-19,-26,-28,-29,-31,-35,-59,-18,-20,-21,-30,-32,-33,-36,-37,-39,-57,-22,-34,-38,-41,-40,-42,-55,-56,-70,]),'FOCAL':([0,2,3,4,5,6,8,28,34,38,40,41,42,43,59,60,63,67,71,72,74,76,77,92,94,99,115,116,117,119,123,124,131,140,141,146,147,149,153,154,155,163,168,169,170,172,173,174,175,177,183,185,186,187,188,189,190,191,192,194,196,198,199,200,201,202,205,208,214,215,],[33,33,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-23,-43,-45,-64,-67,-15,-25,-24,-27,-51,-16,-17,-19,-26,-28,-29,-31,-35,-59,-18,-20,-21,-30,-32,-33,-36,-37,-39,-57,-22,-34,-38,-41,-40,-42,-55,-56,-70,]),'WEB':([0,2,3,4,5,6,8,28,34,38,40,41,42,43,59,60,63,67,71,72,74,76,77,92,94,99,115,116,117,119,123,124,131,140,141,146,147,149,153,154,155,163,168,169,170,172,173,174,175,177,183,185,186,187,188,189,190,191,192,194,196,198,199,200,201,202,205,208,214,215,],[34,34,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-23,-43,-45,-64,-67,-15,-25,-24,-27,-51,-16,-17,-19,-26,-28,-29,-31,-35,-59,-18,-20,-21,-30,-32,-33,-36,-37,-39,-57,-22,-34,-38,-41,-40,-42,-55,-56,-70,]),'TEXTURE':([0,2,3,4,5,6,8,28,34,38,40,41,42,43,59,60,63,67,71,72,74,76,77,92,94,99,115,116,117,119,123,124,131,140,141,146,147,149,153,154,155,163,168,169,170,172,173,174,175,177,183,185,186,187,188,189,190,191,192,194,196,198,199,200,201,202,205,208,214,215,],[35,35,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-23,-43,-45,-64,-67,-15,-25,-24,-27,-51,-16,-17,-19,-26,-28,-29,-31,-35,-59,-18,-20,-21,-30,-32,-33,-36,-37,-39,-57,-22,-34,-38,-41,-40,-42,-55,-56,-70,]),'DOUBLE':([6,9,10,11,12,13,14,15,16,18,22,23,27,32,33,37,38,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,61,62,64,65,66,68,73,75,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,95,96,97,98,102,103,104,105,106,107,108,109,110,111,112,113,114,118,120,121,122,126,127,128,129,130,132,133,134,135,136,137,138,139,142,143,144,145,148,150,151,152,156,157,158,159,160,161,162,164,165,166,167,171,176,178,179,180,181,182,184,193,195,197,203,204,206,207,208,209,210,211,212,213,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,-8,-4,-5,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'STRING':([7,19,39,40,41,42,43,69,100,],[41,41,41,-6,-7,-4,-5,41,41,]),'XYZ':([7,9,10,11,12,13,14,17,19,20,21,24,25,29,30,31,35,38,39,40,41,42,43,69,92,99,100,101,113,115,116,124,125,131,139,149,154,155,169,170,174,175,177,187,190,192,194,201,],[42,42,42,42,42,42,42,58,42,42,42,42,42,42,42,42,42,-8,42,-6,-7,-4,-5,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'ID':([7,9,10,11,12,13,14,19,20,21,24,25,29,30,31,35,38,39,40,41,42,43,69,92,99,100,101,113,115,116,124,125,131,139,149,154,155,169,170,174,175,177,187,190,192,194,201,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,-8,43,-6,-7,-4,-5,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'SHADING_TYPE':([26,],[67,]),'CO':([29,42,43,70,],[69,-4,-5,100,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'input':([0,2,],[1,36,]),'command':([0,2,],[2,2,]),'NUMBER':([6,9,10,11,12,13,14,15,16,18,22,23,27,32,33,37,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,61,62,64,65,66,68,73,75,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,95,96,97,98,102,103,104,105,106,107,108,109,110,111,112,113,114,118,120,121,122,126,127,128,129,130,132,133,134,135,136,137,138,139,142,143,144,145,148,150,151,152,156,157,158,159,160,161,162,164,165,166,167,171,176,178,179,180,181,182,184,193,195,197,203,204,206,207,208,209,210,211,212,213,],[37,44,46,48,50,52,54,56,57,59,63,64,68,73,74,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,118,119,120,121,122,126,127,128,129,130,131,132,133,134,135,136,137,139,142,143,144,145,148,149,150,151,152,154,155,156,157,158,159,160,162,163,164,165,166,167,169,170,171,174,175,176,177,178,179,180,181,182,183,184,187,190,192,193,194,195,196,197,201,203,204,206,207,208,209,210,211,212,213,214,215,]),'TEXT':([7,19,39,69,100,],[39,60,77,99,124,]),'SYMBOL':([7,9,10,11,12,13,14,19,20,21,24,25,29,30,31,35,39,69,92,99,100,101,113,115,116,124,125,131,139,149,154,155,169,170,174,175,177,187,190,192,194,201,],[40,45,47,49,51,53,55,40,61,62,65,66,70,71,72,75,40,40,117,123,40,125,138,140,141,146,147,153,161,168,172,173,185,186,188,189,191,198,199,200,202,205,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> input","S'",1,None,None,None),
  ('input -> <empty>','input',0,'p_input','mdl.py',126),
  ('input -> command input','input',2,'p_input','mdl.py',127),
  ('command -> COMMENT','command',1,'p_command_comment','mdl.py',131),
  ('SYMBOL -> XYZ','SYMBOL',1,'p_SYMBOL','mdl.py',135),
  ('SYMBOL -> ID','SYMBOL',1,'p_SYMBOL','mdl.py',136),
  ('TEXT -> SYMBOL','TEXT',1,'p_TEXT','mdl.py',140),
  ('TEXT -> STRING','TEXT',1,'p_TEXT','mdl.py',141),
  ('NUMBER -> DOUBLE','NUMBER',1,'p_NUMBER','mdl.py',145),
  ('command -> POP','command',1,'p_command_stack','mdl.py',149),
  ('command -> PUSH','command',1,'p_command_stack','mdl.py',150),
  ('command -> SCREEN NUMBER NUMBER','command',3,'p_command_screen','mdl.py',154),
  ('command -> SCREEN','command',1,'p_command_screen','mdl.py',155),
  ('command -> SAVE TEXT TEXT','command',3,'p_command_save','mdl.py',162),
  ('command -> DISPLAY','command',1,'p_command_show','mdl.py',166),
  ('command -> CYLINDER NUMBER NUMBER NUMBER NUMBER NUMBER','command',6,'p_command_cylinder','mdl.py',170),
  ('command -> CYLINDER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',7,'p_command_cylinder','mdl.py',171),
  ('command -> CYLINDER SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_cylinder','mdl.py',172),
  ('command -> CYLINDER SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',8,'p_command_cylinder','mdl.py',173),
  ('command -> HOLLOW_CYLINDER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_hollow_cylinder','mdl.py',187),
  ('command -> HOLLOW_CYLINDER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',8,'p_command_hollow_cylinder','mdl.py',188),
  ('command -> HOLLOW_CYLINDER SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',8,'p_command_hollow_cylinder','mdl.py',189),
  ('command -> HOLLOW_CYLINDER SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',9,'p_command_hollow_cylinder','mdl.py',190),
  ('command -> SPHERE NUMBER NUMBER NUMBER NUMBER','command',5,'p_command_sphere','mdl.py',204),
  ('command -> SPHERE SYMBOL NUMBER NUMBER NUMBER NUMBER','command',6,'p_command_sphere','mdl.py',205),
  ('command -> SPHERE NUMBER NUMBER NUMBER NUMBER SYMBOL','command',6,'p_command_sphere','mdl.py',206),
  ('command -> SPHERE SYMBOL NUMBER NUMBER NUMBER NUMBER SYMBOL','command',7,'p_command_sphere','mdl.py',207),
  ('command -> TORUS NUMBER NUMBER NUMBER NUMBER NUMBER','command',6,'p_command_torus','mdl.py',221),
  ('command -> TORUS NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',7,'p_command_torus','mdl.py',222),
  ('command -> TORUS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_torus','mdl.py',223),
  ('command -> TORUS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',8,'p_command_torus','mdl.py',224),
  ('command -> BOX NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_box','mdl.py',238),
  ('command -> BOX NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',8,'p_command_box','mdl.py',239),
  ('command -> BOX SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',8,'p_command_box','mdl.py',240),
  ('command -> BOX SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',9,'p_command_box','mdl.py',241),
  ('command -> LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_line','mdl.py',255),
  ('command -> LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',8,'p_command_line','mdl.py',256),
  ('command -> LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER','command',8,'p_command_line','mdl.py',257),
  ('command -> LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOL','command',9,'p_command_line','mdl.py',258),
  ('command -> LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',8,'p_command_line','mdl.py',259),
  ('command -> LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',9,'p_command_line','mdl.py',260),
  ('command -> LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER','command',9,'p_command_line','mdl.py',261),
  ('command -> LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOL','command',10,'p_command_line','mdl.py',262),
  ('command -> MOVE NUMBER NUMBER NUMBER SYMBOL','command',5,'p_command_move','mdl.py',283),
  ('command -> MOVE NUMBER NUMBER NUMBER','command',4,'p_command_move','mdl.py',284),
  ('command -> SCALE NUMBER NUMBER NUMBER SYMBOL','command',5,'p_command_scale','mdl.py',292),
  ('command -> SCALE NUMBER NUMBER NUMBER','command',4,'p_command_scale','mdl.py',293),
  ('command -> ROTATE XYZ NUMBER SYMBOL','command',4,'p_command_rotate','mdl.py',301),
  ('command -> ROTATE XYZ NUMBER','command',3,'p_command_rotate','mdl.py',302),
  ('command -> FRAMES NUMBER','command',2,'p_command_frames','mdl.py',310),
  ('command -> BASENAME TEXT','command',2,'p_command_basename','mdl.py',315),
  ('command -> VARY SYMBOL NUMBER NUMBER NUMBER NUMBER','command',6,'p_command_vary','mdl.py',320),
  ('command -> SET SYMBOL NUMBER','command',3,'p_command_knobs','mdl.py',326),
  ('command -> SET_KNOBS NUMBER','command',2,'p_command_knobs','mdl.py',327),
  ('command -> AMBIENT NUMBER NUMBER NUMBER','command',4,'p_command_ambient','mdl.py',338),
  ('command -> CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',11,'p_command_constants','mdl.py',344),
  ('command -> CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',14,'p_command_constants','mdl.py',345),
  ('command -> LIGHT SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',8,'p_command_light','mdl.py',351),
  ('command -> SHADING SHADING_TYPE','command',2,'p_command_shading','mdl.py',357),
  ('command -> CAMERA NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_camera','mdl.py',363),
  ('command -> GENERATE_RAYFILES','command',1,'p_command_generate_rayfiles','mdl.py',368),
  ('command -> MESH CO TEXT','command',3,'p_command_mesh','mdl.py',372),
  ('command -> MESH SYMBOL CO TEXT','command',4,'p_command_mesh','mdl.py',373),
  ('command -> MESH CO TEXT SYMBOL','command',4,'p_command_mesh','mdl.py',374),
  ('command -> MESH SYMBOL CO TEXT SYMBOL','command',5,'p_command_mesh','mdl.py',375),
  ('command -> SAVE_KNOBS SYMBOL','command',2,'p_save_knobs','mdl.py',389),
  ('command -> SAVE_COORDS SYMBOL','command',2,'p_save_coords','mdl.py',395),
  ('command -> TWEEN NUMBER NUMBER SYMBOL SYMBOL','command',5,'p_tween','mdl.py',402),
  ('command -> FOCAL NUMBER','command',2,'p_focal','mdl.py',407),
  ('command -> WEB','command',1,'p_web','mdl.py',411),
  ('command -> TEXTURE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',14,'p_texture','mdl.py',415),
]
