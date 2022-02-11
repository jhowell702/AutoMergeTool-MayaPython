# Import the Maya commands library
from maya import cmds

# default merge distance
mergeDistance = .01

def showWindow():
    
    #create window
    window = cmds.window( title="Auto Merge Tool", iconName='AMT', widthHeight=(275, 150) )
    #column layout
    cmds.columnLayout( adjustableColumn=True )
    #row layout for merge and clean controls
    cmds.rowLayout(numberOfColumns=3)

    cmds.button( label='Merge and Clean', command=lambda x: mergeAndClean() )
    cmds.text( 'Merge Distance' )
    
    #text field setup
    textField = cmds.textField()

    cmds.textField( textField, it='.01',edit=True, aie=True, changeCommand=lambda x: setMergeDistance(textField) )

    cmds.setParent('..')

    #combine buttons without merging vertices
    cmds.button( label='Merge and Delete History', command=mergeDeleteHistory )

    cmds.button( label='Merge and Keep History', command=mergeKeepHistory )

    cmds.button( label='Close', command=('cmds.deleteUI(\"' + window + '\", window=True)') )

    cmds.setParent( '..' )

    cmds.showWindow( window )

def mergeKeepHistory(*args):
    cmds.polyUnite()

def setMergeDistance(*args):

    global mergeDistance
    mergeDistance = cmds.textField(args[0], q=1, text=1)
    

def mergeDeleteHistory(*args):
    cmds.polyUnite()
    cmds.delete(cmds.ls(sl=True)[0], ch=True)

def mergeAndClean(*args):
    cmds.polyUnite()
    cmds.delete(cmds.ls(sl=True)[0], ch=True)
    name = cmds.ls(sl=True)[0]
    verts = cmds.ls(name + '.vtx[*]', fl=True)
    cmds.undoInfo(ock=True)
    for v in verts:
        cmds.select(v, add=True)
    cmds.undoInfo(cck=True)
    cmds.polyMergeVertex(d=mergeDistance)
