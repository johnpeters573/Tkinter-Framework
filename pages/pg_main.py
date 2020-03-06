import sys
sys.path.append("..")
sys.path.append("../plugins")
sys.path.append("../functions")
sys.path.append("../system")

## IMPORT PLUGINS AND MODULES
import g, gui, styles
from types import SimpleNamespace as sn
import os, importlib
from tkinter import IntVar


radiobutton_var = IntVar()

def page(arg):

    ## SAVE PROPERTIES
    arg.hprops = sn(**{}); arg.hobjs = sn(**{}); arg.hvars = sn(**{})
    arg.hprops.__dict__[arg.curpage] = sn(**{});
    arg.hobjs.__dict__[arg.curpage] = sn(**{});
    arg.hvars.__dict__[arg.curpage] = sn(**{});
    
    h = sn(**{})
    ####################### GUI ELEMENTS START #########################

    h.myEntry = sn(**{ ## gui.entry(arg,"style","align","text", name="entryName" ,password=True, keyboard=True, type=number),
        "obj": gui.entry(arg,"entryMedium","center","Edit me!", name="myEntry", password=True, keyboard=True),
        "pos": sn(**{
            "x": 10,
            "y": 10,
            "w": 150,
            "h": 30,
        })
    })

    h.label1 = sn(**{ ## gui.label(arg,"style","align","text")
       "obj": gui.label(arg,"labelSmall","center","Hello There!"),                
       "pos": sn(**{
           "x": 100,
           "y": 300,
           "w": 100,
           "h": 40,
       })
    })

    # h.checkbox = sn(**{ ## gui.checkbox(arg,"yourText", lambda: test(arg)),
    #     "obj": gui.checkbox(arg,"yourText", lambda: test(arg)),
    #     "pos": sn(**{
    #         "x": 10,
    #         "y": 10,
    #         "w": 150,
    #         "h": 30,
    #     })
    # })

    h.checkbox = sn(**{ ## gui.checkbox(arg,"yourText", lambda: test(arg)),
        "obj": gui.checkbox(arg,"yourText", lambda: test(arg,1)),
        "pos": sn(**{
            "x": 10,
            "y": 40,
            "w": 150,
            "h": 30,
        })
    })


    optionList1 = ('a','a' ,'b', 'c')
    h.combobox = sn(**{ ## ttk.OptionMenu(arg.master,v1,*optionList1, command=lambda selected:test123123(selected))
        "obj": gui.combobox(arg,optionList1,lambda selected_val:test(arg,selected_val)),
        "pos": sn(**{
            "x": 10,
            "y": 80,
            "w": 150,
            "h": 30,
        })
    })

    h.progress = sn(**{ ## tttk.Progressbar(arg.master, orient = orient, length = length, mode = mode)
        "obj": gui.progressbar(arg),
        "pos": sn(**{
            "x": 10,
            "y": 120,
            "w": 150,
            "h": 30,
        })
    })

    
    h.radiobutton = sn(**{ ## Radiobutton(arg.master,text="t",padx = 20, variable=v, command=command,value=value).pack(anchor=tk.W)
        "obj": gui.radiobutton(arg,text="option1",variable=radiobutton_var,value=1,command=lambda: test(arg,1)),
        "pos": sn(**{
            "x": 10,
            "y": 160,
            "w": 150,
            "h": 30,
        })
    })

    h.radiobutton2 = sn(**{ ## Radiobutton(arg.master,text="t",padx = 20, variable=v, command=command,value=value).pack(anchor=tk.W)
        "obj": gui.radiobutton(arg,text="option1",variable=radiobutton_var,value=2,command=lambda: test(arg,1)),
        "pos": sn(**{
            "x": 10,
            "y": 200,
            "w": 150,
            "h": 30,
        })
    })





    ####################### GUI ELEMENTS END #########################
    gui.hpropsobjs(arg,h)
    return h


def test(arg, selected):

	print(selected)

	myh = arg.handles.pg_main
	print(myh.checkbox.obj.state())
	if arg.handles.pg_main.checkbox.obj.instate(['selected']):
		print("selected")
	else:
		print("Not selected")
	# print("value: ", gui.checkbox_val(arg.handles.pg_main.checkbox.obj))
	
	# print()
	# start(arg)
	import _thread as thread
	# thread.start_new_thread( start,(arg,) )

	# print(myh.radiobutton.obj['value'])
	# print(myh.radiobutton2.obj['value'])
	# myh.radiobutton2.obj.set('')
	print(radiobutton_var.get())
	# print(myh.radiobutton2.obj.deselect())


def start(arg):
	import time 
	myh = arg.handles.pg_main
	x = 1
	for x in range(100):
		myh.progress.obj['value'] = x
		# arg.master.update_idletasks() 
		arg.master.update()
		time.sleep(0.1) 
		# print(x)

	# myh.progress['value'] = 40
	# arg.master.update_idletasks() 
	# time.sleep(1) 

	# myh.progress['value'] = 50
	# arg.master.update_idletasks() 
	# time.sleep(1) 

	# myh.progress['value'] = 60
	# arg.master.update_idletasks() 
	# time.sleep(1) 

	# myh.progress['value'] = 80
	# arg.master.update_idletasks() 
	# time.sleep(1) 
	# myh.progress['value'] = 100




### RUN THIS FILE FOR QUICK VIEWING ###    
if __name__ == "__main__":
    arg = sn(**{})
    arg.quickpreview = True
    
    arg.curpage = os.path.basename(__file__)[0:-3]
    fcnFilename = "fcn_" + arg.curpage[3:]
    
    gui.setupMaster(arg)
    styles.setup()
    
    arg.handles = sn(**{ arg.curpage : page(arg)})
    arg.__dict__[fcnFilename] = importlib.import_module("functions." + fcnFilename)
#    fcn = arg.__dict__[fcnFilename].preshow(arg)
#    gui.dbgview(arg, fcn, preshow=True )
    gui.showPage(arg,arg.curpage)
    arg.master.mainloop()
    
