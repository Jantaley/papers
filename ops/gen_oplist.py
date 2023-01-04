#coding=utf-8
import numpy as np
import pandas as pd
import json as js
import excel2json

idata = pd.read_excel("Caffe_op_list.xlsx", sheet_name="Sheet1")
idata = idata.fillna( method='ffill', axis=0 )
keys = ['算子名称', 'Classify', 'Name', 'Type Range', 'Required', 'Doc', '规格限制']
op = {
	"operator0":{
	#	"name0":{
	#		"classify":"INPUT",
	#		"type_range":"",
	#		"required":""
	#	},
	#	"name1":{
	#		"classify":"OUTPUT",
	#		"type_range":"",
	#		"required":""
	#	},
		"name2":{
			"classify":"ATTR",
			"type_range":"",
			"required":"",
			"doc":"",
			"limits":""
		}
	}
}
caffeop=dict({})
c_op=dict({})
temp=""
for i in range(len(idata[keys[0]])):
	opname    = idata[keys[0]][i]
	classify  = idata[keys[1]][i]
	var_name  = idata[keys[2]][i]
	type_range= idata[keys[3]][i]
	required  = idata[keys[4]][i]
	doc       = idata[keys[5]][i]
	limits	  = idata[keys[6]][i]
	if (opname==temp):
		c_op[opname].update(dict({ var_name:{
		"classify":classify,
		"type_range":type_range,
		"required":required,
		"doc":doc,
		"limits":limits
		}  }))	
	else:
		temp=opname
		caffeop.update(dict(c_op))
		c_op=dict({})
		c_op.update(dict({opname:{ var_name:{
		"classify":classify,
		"type_range":type_range,
		"required":required,
		"doc":doc,
		"limits":limits
		}  }}))	

with open('caffe_op.json', 'w', encoding='utf-8') as f:
    js.dump(caffeop, f, ensure_ascii=False, indent=4)
#    f.write("laskdfjljsadf")




