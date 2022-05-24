
# apacheparsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'T_COMMENT T_CONFIG_DIRECTIVE T_CONFIG_DIRECTIVE_ARGUMENT T_CONFIG_DIRECTIVE_TAG T_CONFIG_DIRECTIVE_TAG_CLOSE T_QUOTE_DOUBLEconfig_lines : comment\n                        | config_lines comment\n                        | config_directive_with_argument\n                        | config_lines config_directive_with_argument\n                        | config_directive_tag_token\n                        | config_lines config_directive_tag_tokencomment : T_COMMENTconfig_directive_with_argument : config_directive_token config_directive_argument_listconfig_directive_token : T_CONFIG_DIRECTIVEconfig_directive_tag_token : config_directive_tag_token_open\n                                      | config_directive_tag_token_closeconfig_directive_tag_token_open : T_CONFIG_DIRECTIVE_TAGconfig_directive_tag_token_close : T_CONFIG_DIRECTIVE_TAG_CLOSEconfig_directive_argument_list : config_directive_argument_not_quoted_list\n                                          | config_directive_argument_quoted_list\n                                          | config_directive_argument_list config_directive_argument_not_quoted_list\n                                          | config_directive_argument_list config_directive_argument_quoted_listconfig_directive_argument_quoted_list : config_directive_quoted_token config_directive_argument_not_quoted_list config_directive_quoted_tokenconfig_directive_argument_not_quoted_list : config_directive_argument_token\n                                                     | config_directive_argument_not_quoted_list config_directive_argument_tokenconfig_directive_quoted_token : T_QUOTE_DOUBLEconfig_directive_argument_token : T_CONFIG_DIRECTIVE_ARGUMENT'
    
_lr_action_items = {'T_COMMENT':([0,1,2,3,4,5,7,8,10,11,12,13,14,15,16,17,18,20,21,22,23,24,26,],[5,5,-1,-3,-5,-7,-10,-11,-12,-13,-2,-4,-6,-8,-14,-15,-19,-22,-21,-16,-17,-20,-18,]),'T_CONFIG_DIRECTIVE':([0,1,2,3,4,5,7,8,10,11,12,13,14,15,16,17,18,20,21,22,23,24,26,],[9,9,-1,-3,-5,-7,-10,-11,-12,-13,-2,-4,-6,-8,-14,-15,-19,-22,-21,-16,-17,-20,-18,]),'T_CONFIG_DIRECTIVE_TAG':([0,1,2,3,4,5,7,8,10,11,12,13,14,15,16,17,18,20,21,22,23,24,26,],[10,10,-1,-3,-5,-7,-10,-11,-12,-13,-2,-4,-6,-8,-14,-15,-19,-22,-21,-16,-17,-20,-18,]),'T_CONFIG_DIRECTIVE_TAG_CLOSE':([0,1,2,3,4,5,7,8,10,11,12,13,14,15,16,17,18,20,21,22,23,24,26,],[11,11,-1,-3,-5,-7,-10,-11,-12,-13,-2,-4,-6,-8,-14,-15,-19,-22,-21,-16,-17,-20,-18,]),'$end':([1,2,3,4,5,7,8,10,11,12,13,14,15,16,17,18,20,21,22,23,24,26,],[0,-1,-3,-5,-7,-10,-11,-12,-13,-2,-4,-6,-8,-14,-15,-19,-22,-21,-16,-17,-20,-18,]),'T_CONFIG_DIRECTIVE_ARGUMENT':([6,9,15,16,17,18,19,20,21,22,23,24,25,26,],[20,-9,20,20,-15,-19,20,-22,-21,20,-17,-20,20,-18,]),'T_QUOTE_DOUBLE':([6,9,15,16,17,18,20,21,22,23,24,25,26,],[21,-9,21,-14,-15,-19,-22,-21,-16,-17,-20,21,-18,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'config_lines':([0,],[1,]),'comment':([0,1,],[2,12,]),'config_directive_with_argument':([0,1,],[3,13,]),'config_directive_tag_token':([0,1,],[4,14,]),'config_directive_token':([0,1,],[6,6,]),'config_directive_tag_token_open':([0,1,],[7,7,]),'config_directive_tag_token_close':([0,1,],[8,8,]),'config_directive_argument_list':([6,],[15,]),'config_directive_argument_not_quoted_list':([6,15,19,],[16,22,25,]),'config_directive_argument_quoted_list':([6,15,],[17,23,]),'config_directive_argument_token':([6,15,16,19,22,25,],[18,18,24,18,24,24,]),'config_directive_quoted_token':([6,15,25,],[19,19,26,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> config_lines","S'",1,None,None,None),
  ('config_lines -> comment','config_lines',1,'p_config_directive','apache.py',145),
  ('config_lines -> config_lines comment','config_lines',2,'p_config_directive','apache.py',146),
  ('config_lines -> config_directive_with_argument','config_lines',1,'p_config_directive','apache.py',147),
  ('config_lines -> config_lines config_directive_with_argument','config_lines',2,'p_config_directive','apache.py',148),
  ('config_lines -> config_directive_tag_token','config_lines',1,'p_config_directive','apache.py',149),
  ('config_lines -> config_lines config_directive_tag_token','config_lines',2,'p_config_directive','apache.py',150),
  ('comment -> T_COMMENT','comment',1,'p_comment_line','apache.py',154),
  ('config_directive_with_argument -> config_directive_token config_directive_argument_list','config_directive_with_argument',2,'p_config_directive_with_argument','apache.py',158),
  ('config_directive_token -> T_CONFIG_DIRECTIVE','config_directive_token',1,'p_config_directive_token','apache.py',162),
  ('config_directive_tag_token -> config_directive_tag_token_open','config_directive_tag_token',1,'p_config_directive_tag_token','apache.py',166),
  ('config_directive_tag_token -> config_directive_tag_token_close','config_directive_tag_token',1,'p_config_directive_tag_token','apache.py',167),
  ('config_directive_tag_token_open -> T_CONFIG_DIRECTIVE_TAG','config_directive_tag_token_open',1,'p_config_directive_tag_token_open','apache.py',171),
  ('config_directive_tag_token_close -> T_CONFIG_DIRECTIVE_TAG_CLOSE','config_directive_tag_token_close',1,'p_config_directive_tag_token_close','apache.py',189),
  ('config_directive_argument_list -> config_directive_argument_not_quoted_list','config_directive_argument_list',1,'p_config_directive_argument_list','apache.py',195),
  ('config_directive_argument_list -> config_directive_argument_quoted_list','config_directive_argument_list',1,'p_config_directive_argument_list','apache.py',196),
  ('config_directive_argument_list -> config_directive_argument_list config_directive_argument_not_quoted_list','config_directive_argument_list',2,'p_config_directive_argument_list','apache.py',197),
  ('config_directive_argument_list -> config_directive_argument_list config_directive_argument_quoted_list','config_directive_argument_list',2,'p_config_directive_argument_list','apache.py',198),
  ('config_directive_argument_quoted_list -> config_directive_quoted_token config_directive_argument_not_quoted_list config_directive_quoted_token','config_directive_argument_quoted_list',3,'p_config_directive_argument_quoted_list','apache.py',202),
  ('config_directive_argument_not_quoted_list -> config_directive_argument_token','config_directive_argument_not_quoted_list',1,'p_config_directive_argument_not_quoted_list','apache.py',206),
  ('config_directive_argument_not_quoted_list -> config_directive_argument_not_quoted_list config_directive_argument_token','config_directive_argument_not_quoted_list',2,'p_config_directive_argument_not_quoted_list','apache.py',207),
  ('config_directive_quoted_token -> T_QUOTE_DOUBLE','config_directive_quoted_token',1,'p_config_directive_quote','apache.py',211),
  ('config_directive_argument_token -> T_CONFIG_DIRECTIVE_ARGUMENT','config_directive_argument_token',1,'p_config_directive_argument_token','apache.py',219),
]
