import wx
from Panels import Start, Analyze, Validate


class HomeFrame(wx.Frame):
    
    """
    main frame for the slip detector
    """

    def __init__(self, *args, **kw):
        

        super(HomeFrame, self).__init__(*args, **kw)


        self.StartPanel = Start.StartPanel(self)
        self.StartPanel.Hide()

        self.AnalyzePanel = Analyze.AnalyzePanel(self)
        self.AnalyzePanel.Hide()
        
        self.ValidatePanel = Validate.ValidatePanel(self)
        self.ValidatePanel.Hide()


        self.current_panel = self.ValidatePanel
        

        # configure UI organization
        self.main_sizer = wx.GridBagSizer(0, 0)
        self.main_sizer.SetEmptyCellSize((0, 0))
        self.main_sizer.Add(self.current_panel, pos=(0, 0), span = (5, 5), flag=wx.EXPAND)
        self.SetSizer(self.main_sizer)

        # create a menu bar
        self.makeMenuBar()

        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("Slip detector ready for new job")

        self.current_panel.Show()


    def makeMenuBar(self):
        """
        more functions / menu items can be added
        for additional features
        """

        ################################################################

        file_menu = wx.Menu()
        

        start_item = file_menu.Append(-1, "&Home page...\tCtrl-H",
                "Help string shown in status bar for this menu item")
        import_item = file_menu.Append(-1, "&Import file...\tCtrl-I",
                "Help string shown in status bar for this menu item")
        save_item = file_menu.Append(-1, "&Save...\t",
                "Save analysis result")
        save_as_item = file_menu.Append(-1, "&Save as...\tCtrl-S",
                "Save analysis result as new file")

        file_menu.AppendSeparator() 
        #-----------------------------------

        # When using a stock ID we don't need to specify the menu item's
        # label
        quit_item = file_menu.Append(wx.ID_EXIT)

        ################################################################
        
        action_menu = wx.Menu()
        analyze_item = action_menu.Append(-1, "&Analyze...\tCtrl-N",
                "Predict slips based on csv")
        validate_item = action_menu.Append(-1, "&Validate...\tCtrl-L",
                "Manually validate and correct detected slips")

        ################################################################

        statistics_menu = wx.Menu()
        t_test_item = statistics_menu.Append(-1, "&t-test...\tCtrl-T",
                "Apply t-test to slip statistics")
        anova_item = statistics_menu.Append(-1, "&ANOVA...\tCtrl-A",
                "Apply ANOVA to slip statistics")

        ################################################################

        help_menu = wx.Menu()
        about_item = help_menu.Append(wx.ID_ABOUT)
        help_item = help_menu.Append(wx.ID_HELP)
        contact_item = help_menu.Append(-1, "&Contact us...\tCtrl-O",
                "Contact us for suggestions and support")

        # configure menu_bar

        menu_bar = wx.MenuBar()
        menu_bar.Append(file_menu, "&File")
        menu_bar.Append(action_menu, "&Action")
        menu_bar.Append(statistics_menu, "&Statistics")
        menu_bar.Append(help_menu, "&Help")

        self.SetMenuBar(menu_bar)
        
        # configure events for menu items
        self.Bind(wx.EVT_MENU, self.on_start, start_item)
        self.Bind(wx.EVT_MENU, self.on_about, about_item)
        self.Bind(wx.EVT_MENU, self.on_quit, quit_item)
        self.Bind(wx.EVT_MENU, self.on_analyze, analyze_item)
        self.Bind(wx.EVT_MENU, self.on_validate, validate_item)

    def on_start(self, event):
        
        self.current_panel.Hide()

        self.main_sizer.Replace(self.current_panel, self.StartPanel)
        self.SetSizer(self.main_sizer)

        self.current_panel = self.StartPanel
        self.current_panel.Show()

        self.SetStatusText('Welcome!')
        self.Layout()
        self.Refresh()
    
    def on_import(self, event):
        
        pass


    def on_save_as(self, event):
        
        
        pass


    def on_quit(self, event):

        self.Close(True)


    def on_analyze(self, event):
        
        self.current_panel.Hide()

        self.main_sizer.Replace(self.current_panel, self.AnalyzePanel)
        self.SetSizer(self.main_sizer)

        self.current_panel = self.AnalyzePanel
        self.current_panel.Show()

        self.SetStatusText('Slip detector ready for new job')
        self.Layout()
        self.Refresh()

    
    def on_validate(self, event):

        self.current_panel.Hide()

        self.main_sizer.Replace(self.current_panel, self.ValidatePanel)
        self.SetSizer(self.main_sizer)

        self.current_panel = self.ValidatePanel
        self.current_panel.Show()

        self.SetStatusText('Validating data')
        self.Layout()
        self.Refresh() # refresh to show slider in right proportion
        

    def on_t_test(self, event):

        pass


    def on_anova(self, event):

        pass


    def on_about(self, event):
        
        wx.MessageBox( "This is a slip detector for ladder rung "\
                        "analysis, based on DeepLabCut output of "\
                        "bodypart coordinates (or similarly "\
                        "structured data). Made by Shuqing Zhao.",
                        "About Slip Detector",
                        wx.OK|wx.ICON_INFORMATION)


    def show_img(self):

        png = wx.Image('/home/annette/Desktop/DeepLabCut/jumps.jpg', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self, -1, png, (10, 5), (png.GetWidth(), png.GetHeight()))

    def on_help(self, event):

        pass


    def on_contact(self, event):

        pass





if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.


    from Functions import ConfigFunctions

    configs = ConfigFunctions.load_config('./config.yaml')
    window_width, window_height = configs['window_width'], configs['window_height']

    app = wx.App(redirect = True)
    home_frame = HomeFrame(None, title='Slip Detector', size=(window_width, window_height))
    # test_frame = test_frame.Example(None, title='Slip Detector', size=(1000,800))
    # home_frame.test_frame = test_frame
    # test_frame.Hide()
    # home_frame.Show()
    home_frame.Show()
    app.MainLoop()