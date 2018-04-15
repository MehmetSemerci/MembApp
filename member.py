#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.12
# In conjunction with Tcl version 8.6
#    Apr 15, 2018 05:51:25 AM

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import member_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    member_support.set_Tk_var()
    top = IEEE_METU_NCC_Member_System (root)
    member_support.init(root, top)
    root.mainloop()

w = None
def create_IEEE_METU_NCC_Member_System(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    member_support.set_Tk_var()
    top = IEEE_METU_NCC_Member_System (w)
    member_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_IEEE_METU_NCC_Member_System():
    global w
    w.destroy()
    w = None


class IEEE_METU_NCC_Member_System:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("595x433+575+303")
        top.title("IEEE METU NCC Member System")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.labelBackground = Label(top)
        self.labelBackground.place(relx=-0.01, rely=-0.01, height=411, width=604)

        self.labelBackground.configure(activebackground="#f9f9f9")
        self.labelBackground.configure(activeforeground="black")
        self.labelBackground.configure(background="#d9d9d9")
        self.labelBackground.configure(disabledforeground="#a3a3a3")
        self.labelBackground.configure(foreground="#000000")
        self.labelBackground.configure(highlightbackground="#d9d9d9")
        self.labelBackground.configure(highlightcolor="black")
        self._img1 = PhotoImage(file="../Untitled-1.png")
        self.labelBackground.configure(image=self._img1)
        self.labelBackground.configure(text='''Label''')

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.menubar.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                command=member_support.pushMainMenu,
                font="TkMenuFont",
                foreground="#000000",
                label="Main Menu",
                state=DISABLED)
        self.member_operations = Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.member_operations,
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Member Operations",
                state=DISABLED)
        self.member_operations.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                command=member_support.pushAddMember,
                font="TkMenuFont",
                foreground="#000000",
                label="Add Member")
        self.member_operations.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                command=member_support.pushEditMember,
                font="TkMenuFont",
                foreground="#000000",
                label="Edit / Remove Member")
        self.member_operations.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                command=member_support.pushMemberList,
                font="TkMenuFont",
                foreground="#000000",
                label="Member List")
        self.event_operations = Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.event_operations,
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Event Operations",
                state=DISABLED)
        self.event_operations.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                command=member_support.pushCreateEvent,
                font="TkMenuFont",
                foreground="#000000",
                label="Create Event")
        self.event_operations.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                command=member_support.pushTakeAttend,
                font="TkMenuFont",
                foreground="#000000",
                label="Take Attendance")
        self.event_operations.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                command=member_support.pushEventList,
                font="TkMenuFont",
                foreground="#000000",
                label="Event List")
        self.menubar.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                command=member_support.pushChangePassword,
                font="TkMenuFont",
                foreground="#000000",
                label="Change Password",
                state=DISABLED)


        self.buttonLogout = ttk.Button(top)
        self.buttonLogout.place(relx=-0.01, rely=0.93, height=30, width=606)
        self.buttonLogout.configure(command=member_support.pushLogout)
        self.buttonLogout.configure(takefocus="")
        self.buttonLogout.configure(text='''Logout''')

        self.frameLogin = Frame(top)
        self.frameLogin.place(relx=-0.01, rely=-0.02, relheight=1.05
                , relwidth=1.01)
        self.frameLogin.configure(relief=GROOVE)
        self.frameLogin.configure(borderwidth="2")
        self.frameLogin.configure(relief=GROOVE)
        self.frameLogin.configure(background="#d9d9d9")
        self.frameLogin.configure(highlightbackground="#d9d9d9")
        self.frameLogin.configure(highlightcolor="black")
        self.frameLogin.configure(width=605)

        self.TEntry1 = ttk.Entry(self.frameLogin)
        self.TEntry1.place(relx=0.43, rely=0.37, relheight=0.05, relwidth=0.23)
        self.TEntry1.configure(textvariable=member_support.txtLoginSchoolID)
        self.TEntry1.configure(validate="focusout")
        self.TEntry1.focus()
        self.TEntry1.configure(cursor="ibeam")

        self.TEntry2 = ttk.Entry(self.frameLogin)
        self.TEntry2.place(relx=0.43, rely=0.46, relheight=0.05, relwidth=0.23)
        self.TEntry2.configure(textvariable=member_support.txtLoginPassword)
        self.TEntry2.configure(takefocus="")
        self.TEntry2.configure(show="*")
        self.TEntry2.configure(cursor="ibeam")

        self.TButton2 = ttk.Button(self.frameLogin)
        self.TButton2.place(relx=0.32, rely=0.53, height=30, width=209)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(command=member_support.pushLoginButton)
        self.TButton2.configure(text='''Login''')
        self.TButton2.bind('<Return>',lambda e:member_support.loginButtonReturn(e))

        self.TLabel1 = ttk.Label(self.frameLogin)
        self.TLabel1.place(relx=0.32, rely=0.37, height=19, width=60)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief=FLAT)
        self.TLabel1.configure(text='''School ID :''')

        self.TLabel2 = ttk.Label(self.frameLogin)
        self.TLabel2.place(relx=0.32, rely=0.46, height=19, width=60)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font="TkDefaultFont")
        self.TLabel2.configure(relief=FLAT)
        self.TLabel2.configure(text='''Password :''')

        self.frameAddMember = Frame(top)
        self.frameAddMember.place(relx=-0.01, rely=-0.02, relheight=0
                , relwidth=0)
        self.frameAddMember.configure(relief=GROOVE)
        self.frameAddMember.configure(borderwidth="2")
        self.frameAddMember.configure(relief=GROOVE)
        self.frameAddMember.configure(background="#d9d9d9")
        self.frameAddMember.configure(highlightbackground="#d9d9d9")
        self.frameAddMember.configure(highlightcolor="black")
        self.frameAddMember.configure(width=605)

        self.TEntry3 = ttk.Entry(self.frameAddMember)
        self.TEntry3.place(relx=0.41, rely=0.27, relheight=0.05, relwidth=0.21)
        self.TEntry3.configure(textvariable=member_support.txtAddUID)
        self.TEntry3.configure(cursor="ibeam")
        self.TEntry3.bind('<Return>',lambda e:member_support.addUIDReturn(e))

        self.TEntry4 = ttk.Entry(self.frameAddMember)
        self.TEntry4.place(relx=0.41, rely=0.36, relheight=0.05, relwidth=0.21)
        self.TEntry4.configure(textvariable=member_support.txtAddName)
        self.TEntry4.configure(takefocus="")
        self.TEntry4.configure(cursor="ibeam")

        self.TEntry5 = ttk.Entry(self.frameAddMember)
        self.TEntry5.place(relx=0.41, rely=0.44, relheight=0.05, relwidth=0.21)
        self.TEntry5.configure(textvariable=member_support.txtAddSurname)
        self.TEntry5.configure(takefocus="")
        self.TEntry5.configure(cursor="ibeam")

        self.TEntry6 = ttk.Entry(self.frameAddMember)
        self.TEntry6.place(relx=0.41, rely=0.53, relheight=0.05, relwidth=0.21)
        self.TEntry6.configure(textvariable=member_support.txtAddSchoolID)
        self.TEntry6.configure(takefocus="")
        self.TEntry6.configure(cursor="ibeam")

        self.TEntry7 = ttk.Entry(self.frameAddMember)
        self.TEntry7.place(relx=0.41, rely=0.62, relheight=0.05, relwidth=0.21)
        self.TEntry7.configure(textvariable=member_support.txtAddPhone)
        self.TEntry7.configure(takefocus="")
        self.TEntry7.configure(cursor="ibeam")

        self.buttonAddMember = ttk.Button(self.frameAddMember)
        self.buttonAddMember.place(relx=0.32, rely=0.7, height=30, width=190)
        self.buttonAddMember.configure(command=member_support.pushAddMemberButton)
        self.buttonAddMember.configure(takefocus="")
        self.buttonAddMember.configure(text='''Add''')
        self.buttonAddMember.bind('<Return>',lambda e:member_support.buttonAddReturn(e))

        self.TLabel3 = ttk.Label(self.frameAddMember)
        self.TLabel3.place(relx=0.36, rely=0.27, height=19, width=29)
        self.TLabel3.configure(background="#d9d9d9")
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(font="TkDefaultFont")
        self.TLabel3.configure(relief=FLAT)
        self.TLabel3.configure(text='''UID :''')

        self.TLabel4 = ttk.Label(self.frameAddMember)
        self.TLabel4.place(relx=0.33, rely=0.36, height=19, width=42)
        self.TLabel4.configure(background="#d9d9d9")
        self.TLabel4.configure(foreground="#000000")
        self.TLabel4.configure(font="TkDefaultFont")
        self.TLabel4.configure(relief=FLAT)
        self.TLabel4.configure(text='''Name :''')

        self.TLabel5 = ttk.Label(self.frameAddMember)
        self.TLabel5.place(relx=0.31, rely=0.44, height=19, width=57)
        self.TLabel5.configure(background="#d9d9d9")
        self.TLabel5.configure(foreground="#000000")
        self.TLabel5.configure(font="TkDefaultFont")
        self.TLabel5.configure(relief=FLAT)
        self.TLabel5.configure(text='''Surname :''')

        self.TLabel6 = ttk.Label(self.frameAddMember)
        self.TLabel6.place(relx=0.31, rely=0.53, height=19, width=60)
        self.TLabel6.configure(background="#d9d9d9")
        self.TLabel6.configure(foreground="#000000")
        self.TLabel6.configure(font="TkDefaultFont")
        self.TLabel6.configure(relief=FLAT)
        self.TLabel6.configure(text='''School ID :''')

        self.TLabel7 = ttk.Label(self.frameAddMember)
        self.TLabel7.place(relx=0.33, rely=0.62, height=19, width=44)
        self.TLabel7.configure(background="#d9d9d9")
        self.TLabel7.configure(foreground="#000000")
        self.TLabel7.configure(font="TkDefaultFont")
        self.TLabel7.configure(relief=FLAT)
        self.TLabel7.configure(text='''Phone :''')

        self.TLabel8 = ttk.Label(self.frameAddMember)
        self.TLabel8.place(relx=0.32, rely=0.81, height=19, width=196)
        self.TLabel8.configure(background="#d9d9d9")
        self.TLabel8.configure(foreground="#000000")
        self.TLabel8.configure(font="TkDefaultFont")
        self.TLabel8.configure(relief=FLAT)
        self.TLabel8.configure(textvariable=member_support.txtLabelAddInfo)

        self.frameEditMember = Frame(top)
        self.frameEditMember.place(relx=-0.01, rely=-0.02, relheight=0
                , relwidth=0)
        self.frameEditMember.configure(relief=GROOVE)
        self.frameEditMember.configure(borderwidth="2")
        self.frameEditMember.configure(relief=GROOVE)
        self.frameEditMember.configure(background="#d9d9d9")
        self.frameEditMember.configure(highlightbackground="#d9d9d9")
        self.frameEditMember.configure(highlightcolor="black")
        self.frameEditMember.configure(width=125)

        self.TEntry8 = ttk.Entry(self.frameEditMember)
        self.TEntry8.place(relx=0.4, rely=0.2, relheight=0.05, relwidth=0.21)
        self.TEntry8.configure(textvariable=member_support.txtEditNum)
        self.TEntry8.configure(takefocus="")
        self.TEntry8.configure(cursor="ibeam")

        self.entryEditUID = ttk.Entry(self.frameEditMember)
        self.entryEditUID.place(relx=0.4, rely=0.29, relheight=0.05
                , relwidth=0.21)
        READONLY = 'readonly'
        self.entryEditUID.configure(state=READONLY)
        self.entryEditUID.configure(textvariable=member_support.txtEditUID)
        self.entryEditUID.configure(takefocus="")
        self.entryEditUID.configure(cursor="ibeam")

        self.entryEditName = ttk.Entry(self.frameEditMember)
        self.entryEditName.place(relx=0.4, rely=0.37, relheight=0.05
                , relwidth=0.21)
        READONLY = 'readonly'
        self.entryEditName.configure(state=READONLY)
        self.entryEditName.configure(textvariable=member_support.txtEditName)
        self.entryEditName.configure(takefocus="")
        self.entryEditName.configure(cursor="ibeam")

        self.entryEditSurname = ttk.Entry(self.frameEditMember)
        self.entryEditSurname.place(relx=0.4, rely=0.46, relheight=0.05
                , relwidth=0.21)
        READONLY = 'readonly'
        self.entryEditSurname.configure(state=READONLY)
        self.entryEditSurname.configure(textvariable=member_support.txtEditSurname)
        self.entryEditSurname.configure(takefocus="")
        self.entryEditSurname.configure(cursor="ibeam")

        self.entryEditSchool = ttk.Entry(self.frameEditMember)
        self.entryEditSchool.place(relx=0.4, rely=0.55, relheight=0.05
                , relwidth=0.21)
        READONLY = 'readonly'
        self.entryEditSchool.configure(state=READONLY)
        self.entryEditSchool.configure(textvariable=member_support.txtEditSchoolID)
        self.entryEditSchool.configure(takefocus="")
        self.entryEditSchool.configure(cursor="ibeam")

        self.entryEditPhone = ttk.Entry(self.frameEditMember)
        self.entryEditPhone.place(relx=0.4, rely=0.64, relheight=0.05
                , relwidth=0.21)
        READONLY = 'readonly'
        self.entryEditPhone.configure(state=READONLY)
        self.entryEditPhone.configure(textvariable=member_support.txtEditPhone)
        self.entryEditPhone.configure(takefocus="")
        self.entryEditPhone.configure(cursor="ibeam")

        self.TButton4 = ttk.Button(self.frameEditMember)
        self.TButton4.place(relx=0.28, rely=0.73, height=25, width=76)
        self.TButton4.configure(command=member_support.pushEditRemove)
        self.TButton4.configure(takefocus="")
        self.TButton4.configure(text='''Remove''')

        self.TButton5 = ttk.Button(self.frameEditMember)
        self.TButton5.place(relx=0.5, rely=0.73, height=25, width=76)
        self.TButton5.configure(command=member_support.pushEditSave)
        self.TButton5.configure(takefocus="")
        self.TButton5.configure(text='''Save''')

        self.TLabel9 = ttk.Label(self.frameEditMember)
        self.TLabel9.place(relx=0.23, rely=0.2, height=19, width=90)
        self.TLabel9.configure(background="#d9d9d9")
        self.TLabel9.configure(foreground="#000000")
        self.TLabel9.configure(font="TkDefaultFont")
        self.TLabel9.configure(relief=FLAT)
        self.TLabel9.configure(text='''UID / School ID :''')

        self.TLabel10 = ttk.Label(self.frameEditMember)
        self.TLabel10.place(relx=0.33, rely=0.29, height=19, width=29)
        self.TLabel10.configure(background="#d9d9d9")
        self.TLabel10.configure(foreground="#000000")
        self.TLabel10.configure(font="TkDefaultFont")
        self.TLabel10.configure(relief=FLAT)
        self.TLabel10.configure(text='''UID :''')

        self.TLabel11 = ttk.Label(self.frameEditMember)
        self.TLabel11.place(relx=0.31, rely=0.37, height=19, width=42)
        self.TLabel11.configure(background="#d9d9d9")
        self.TLabel11.configure(foreground="#000000")
        self.TLabel11.configure(font="TkDefaultFont")
        self.TLabel11.configure(relief=FLAT)
        self.TLabel11.configure(text='''Name :''')

        self.TLabel12 = ttk.Label(self.frameEditMember)
        self.TLabel12.place(relx=0.28, rely=0.46, height=19, width=57)
        self.TLabel12.configure(background="#d9d9d9")
        self.TLabel12.configure(foreground="#000000")
        self.TLabel12.configure(font="TkDefaultFont")
        self.TLabel12.configure(relief=FLAT)
        self.TLabel12.configure(text='''Surname :''')

        self.TLabel13 = ttk.Label(self.frameEditMember)
        self.TLabel13.place(relx=0.28, rely=0.55, height=19, width=60)
        self.TLabel13.configure(background="#d9d9d9")
        self.TLabel13.configure(foreground="#000000")
        self.TLabel13.configure(font="TkDefaultFont")
        self.TLabel13.configure(relief=FLAT)
        self.TLabel13.configure(text='''School ID :''')

        self.TLabel14 = ttk.Label(self.frameEditMember)
        self.TLabel14.place(relx=0.31, rely=0.64, height=19, width=44)
        self.TLabel14.configure(background="#d9d9d9")
        self.TLabel14.configure(foreground="#000000")
        self.TLabel14.configure(font="TkDefaultFont")
        self.TLabel14.configure(relief=FLAT)
        self.TLabel14.configure(text='''Phone :''')

        self.style.map('TCheckbutton',background=
            [('selected', _bgcolor), ('active', _ana2color)])
        self.TCheckbutton1 = ttk.Checkbutton(self.frameEditMember)
        self.TCheckbutton1.place(relx=0.65, rely=0.2, relwidth=0.07
                , relheight=0.0, height=21)
        self.TCheckbutton1.configure(variable=member_support.editCheck)
        self.TCheckbutton1.configure(command=member_support.pushEditCheck)
        self.TCheckbutton1.configure(takefocus="")
        self.TCheckbutton1.configure(text='''Edit''')

        self.TLabel15 = ttk.Label(self.frameEditMember)
        self.TLabel15.place(relx=0.25, rely=0.81, height=19, width=226)
        self.TLabel15.configure(background="#d9d9d9")
        self.TLabel15.configure(foreground="#000000")
        self.TLabel15.configure(font="TkDefaultFont")
        self.TLabel15.configure(relief=FLAT)
        self.TLabel15.configure(textvariable=member_support.txtLabelEditInfo)

        self.frameCreateEvent = Frame(top)
        self.frameCreateEvent.place(relx=-0.01, rely=-0.02, relheight=0
                , relwidth=0)
        self.frameCreateEvent.configure(relief=GROOVE)
        self.frameCreateEvent.configure(borderwidth="2")
        self.frameCreateEvent.configure(relief=GROOVE)
        self.frameCreateEvent.configure(background="#d9d9d9")
        self.frameCreateEvent.configure(highlightbackground="#d9d9d9")
        self.frameCreateEvent.configure(highlightcolor="black")
        self.frameCreateEvent.configure(width=125)

        self.TEntry14 = ttk.Entry(self.frameCreateEvent)
        self.TEntry14.place(relx=0.41, rely=0.24, relheight=0.05, relwidth=0.21)
        self.TEntry14.configure(textvariable=member_support.txtCreateEventName)
        self.TEntry14.configure(takefocus="")
        self.TEntry14.configure(cursor="ibeam")

        self.TEntry15 = ttk.Entry(self.frameCreateEvent)
        self.TEntry15.place(relx=0.41, rely=0.33, relheight=0.05, relwidth=0.21)
        self.TEntry15.configure(textvariable=member_support.txtCreateSociety)
        self.TEntry15.configure(takefocus="")
        self.TEntry15.configure(cursor="ibeam")

        self.TEntry16 = ttk.Entry(self.frameCreateEvent)
        self.TEntry16.place(relx=0.41, rely=0.42, relheight=0.05, relwidth=0.21)
        self.TEntry16.configure(textvariable=member_support.txtCreateDate)
        self.TEntry16.configure(takefocus="")
        self.TEntry16.configure(cursor="ibeam")

        self.TLabel16 = ttk.Label(self.frameCreateEvent)
        self.TLabel16.place(relx=0.28, rely=0.24, height=19, width=74)
        self.TLabel16.configure(background="#d9d9d9")
        self.TLabel16.configure(foreground="#000000")
        self.TLabel16.configure(font="TkDefaultFont")
        self.TLabel16.configure(relief=FLAT)
        self.TLabel16.configure(text='''Event Name :''')

        self.TLabel17 = ttk.Label(self.frameCreateEvent)
        self.TLabel17.place(relx=0.32, rely=0.33, height=19, width=48)
        self.TLabel17.configure(background="#d9d9d9")
        self.TLabel17.configure(foreground="#000000")
        self.TLabel17.configure(font="TkDefaultFont")
        self.TLabel17.configure(relief=FLAT)
        self.TLabel17.configure(text='''Society :''')

        self.TLabel18 = ttk.Label(self.frameCreateEvent)
        self.TLabel18.place(relx=0.35, rely=0.42, height=19, width=34)
        self.TLabel18.configure(background="#d9d9d9")
        self.TLabel18.configure(foreground="#000000")
        self.TLabel18.configure(font="TkDefaultFont")
        self.TLabel18.configure(relief=FLAT)
        self.TLabel18.configure(text='''Date :''')

        self.TButton6 = ttk.Button(self.frameCreateEvent)
        self.TButton6.place(relx=0.28, rely=0.48, height=30, width=206)
        self.TButton6.configure(command=member_support.pushCreateEvent)
        self.TButton6.configure(takefocus="")
        self.TButton6.configure(text='''Create Event''')

        self.TLabel19 = ttk.Label(self.frameCreateEvent)
        self.TLabel19.place(relx=0.3, rely=0.59, height=19, width=196)
        self.TLabel19.configure(background="#d9d9d9")
        self.TLabel19.configure(foreground="#000000")
        self.TLabel19.configure(font="TkDefaultFont")
        self.TLabel19.configure(relief=FLAT)
        self.TLabel19.configure(textvariable=member_support.txtLabelCreateInfo)

        self.frameAttendance = Frame(top)
        self.frameAttendance.place(relx=-0.01, rely=-0.02, relheight=0
                , relwidth=0)
        self.frameAttendance.configure(relief=GROOVE)
        self.frameAttendance.configure(borderwidth="2")
        self.frameAttendance.configure(relief=GROOVE)
        self.frameAttendance.configure(background="#d9d9d9")
        self.frameAttendance.configure(highlightbackground="#d9d9d9")
        self.frameAttendance.configure(highlightcolor="black")
        self.frameAttendance.configure(width=125)

        self.TCombobox1 = ttk.Combobox(self.frameAttendance)
        self.TCombobox1.place(relx=0.45, rely=0.37, relheight=0.05
                , relwidth=0.24)
        self.value_list = ["hello"]
        self.TCombobox1.configure(values=self.value_list)
        self.TCombobox1.configure(textvariable=member_support.combobox)
        self.TCombobox1.configure(takefocus="")

        self.TLabel20 = ttk.Label(self.frameAttendance)
        self.TLabel20.place(relx=0.3, rely=0.37, height=19, width=82)
        self.TLabel20.configure(background="#d9d9d9")
        self.TLabel20.configure(foreground="#000000")
        self.TLabel20.configure(font="TkDefaultFont")
        self.TLabel20.configure(relief=FLAT)
        self.TLabel20.configure(text='''Choose Event :''')

        self.TButton7 = ttk.Button(self.frameAttendance)
        self.TButton7.place(relx=0.3, rely=0.44, height=30, width=236)
        self.TButton7.configure(command=member_support.pushAttendanceOK)
        self.TButton7.configure(takefocus="")
        self.TButton7.configure(text='''OK''')

        self.frameTakeAttend = Frame(self.frameAttendance)
        self.frameTakeAttend.place(relx=0.23, rely=0.29, relheight=0
                , relwidth=0)
        self.frameTakeAttend.configure(relief=GROOVE)
        self.frameTakeAttend.configure(borderwidth="2")
        self.frameTakeAttend.configure(relief=GROOVE)
        self.frameTakeAttend.configure(background="#d9d9d9")
        self.frameTakeAttend.configure(highlightbackground="#d9d9d9")
        self.frameTakeAttend.configure(highlightcolor="black")
        self.frameTakeAttend.configure(width=325)

        self.TEntry17 = ttk.Entry(self.frameTakeAttend)
        self.TEntry17.place(relx=0.37, rely=0.4, relheight=0.12, relwidth=0.42)
        self.TEntry17.configure(takefocus="1")
        self.TEntry17.configure(cursor="ibeam")

        self.TLabel21 = ttk.Label(self.frameTakeAttend)
        self.TLabel21.place(relx=0.15, rely=0.4, height=19, width=57)
        self.TLabel21.configure(background="#d9d9d9")
        self.TLabel21.configure(foreground="#000000")
        self.TLabel21.configure(font="TkDefaultFont")
        self.TLabel21.configure(relief=FLAT)
        self.TLabel21.configure(text='''Card UID :''')

        self.TLabel22 = ttk.Label(self.frameTakeAttend)
        self.TLabel22.place(relx=0.15, rely=0.57, height=19, width=206)
        self.TLabel22.configure(background="#d9d9d9")
        self.TLabel22.configure(foreground="#000000")
        self.TLabel22.configure(font="TkDefaultFont")
        self.TLabel22.configure(relief=FLAT)
        self.TLabel22.configure(textvariable=member_support.txtAttendanceInfo)

        self.framePassword = Frame(top)
        self.framePassword.place(relx=-0.01, rely=-0.02, relheight=0
                , relwidth=0)
        self.framePassword.configure(relief=GROOVE)
        self.framePassword.configure(borderwidth="2")
        self.framePassword.configure(relief=GROOVE)
        self.framePassword.configure(background="#d9d9d9")
        self.framePassword.configure(highlightbackground="#d9d9d9")
        self.framePassword.configure(highlightcolor="black")
        self.framePassword.configure(width=603)

        self.TEntry18 = ttk.Entry(self.framePassword)
        self.TEntry18.place(relx=0.48, rely=0.31, relheight=0.05, relwidth=0.21)
        self.TEntry18.configure(show="*")
        self.TEntry18.configure(takefocus="")
        self.TEntry18.configure(cursor="ibeam")

        self.TEntry19 = ttk.Entry(self.framePassword)
        self.TEntry19.place(relx=0.48, rely=0.4, relheight=0.05, relwidth=0.21)
        self.TEntry19.configure(show="*")
        self.TEntry19.configure(takefocus="")
        self.TEntry19.configure(cursor="ibeam")

        self.TEntry20 = ttk.Entry(self.framePassword)
        self.TEntry20.place(relx=0.48, rely=0.48, relheight=0.05, relwidth=0.21)
        self.TEntry20.configure(show="*")
        self.TEntry20.configure(takefocus="")
        self.TEntry20.configure(cursor="ibeam")

        self.TButton8 = ttk.Button(self.framePassword)
        self.TButton8.place(relx=0.27, rely=0.55, height=30, width=256)
        self.TButton8.configure(command=member_support.pushSavePassword)
        self.TButton8.configure(takefocus="")
        self.TButton8.configure(text='''Save''')

        self.TLabel23 = ttk.Label(self.framePassword)
        self.TLabel23.place(relx=0.3, rely=0.31, height=19, width=103)
        self.TLabel23.configure(background="#d9d9d9")
        self.TLabel23.configure(foreground="#000000")
        self.TLabel23.configure(font="TkDefaultFont")
        self.TLabel23.configure(relief=FLAT)
        self.TLabel23.configure(text='''Current Password :''')

        self.TLabel24 = ttk.Label(self.framePassword)
        self.TLabel24.place(relx=0.32, rely=0.4, height=19, width=87)
        self.TLabel24.configure(background="#d9d9d9")
        self.TLabel24.configure(foreground="#000000")
        self.TLabel24.configure(font="TkDefaultFont")
        self.TLabel24.configure(relief=FLAT)
        self.TLabel24.configure(text='''New Password :''')

        self.TLabel25 = ttk.Label(self.framePassword)
        self.TLabel25.place(relx=0.25, rely=0.48, height=19, width=134)
        self.TLabel25.configure(background="#d9d9d9")
        self.TLabel25.configure(foreground="#000000")
        self.TLabel25.configure(font="TkDefaultFont")
        self.TLabel25.configure(relief=FLAT)
        self.TLabel25.configure(text='''Confirm New Password :''')






if __name__ == '__main__':
    vp_start_gui()



