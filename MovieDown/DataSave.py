import sqlite3

class DataOutput(object):
    def __init__(self):
        self.cx = sqlite3.connect("MTime.db")
        self.create_table("MTime")
        self.datas=[]

    def create_table(self,table_name):
        values = """
        id integer primary key,
        movieId integer,
        movieTitle     varchar(40) NOT NULL, 
        RPictureFinal  REAL NOT NULL DEFAULT 0.0, 
        RStoryFinal    REAL NOT NULL DEFAULT 0.0, 
        RDirectorFinal REAL NOT NULL DEFAULT 0.0, 
        ROtherFinal    REAL NOT NULL DEFAULT 0.0, 
        RatingFinal    REAL NOT NULL DEFAULT 0.0, 
        Usercount      integer NOT NULL DEFAULT 0,
        AttitudeCount  integer NOT NULL DEFAULT 0,
        TotalBoxOffice varchar(20) NOT NULL,
        TodayBoxOffice varchar(20) NOT NULL,
        Rank integer not null default 0,
        ShowDays integer not null default 0,
        isRelease integer not null  
        """
        self.cx.execute("Create table IF Not Exists %s( %s )"%(table_name, values))

    def store_data(self,data):
        if data is None:
            return
        self.datas.append(data)
        if len(self.datas) > 0:
            self.output_db('MTime')

    def output_db(self,table_name):
        for data in self.datas:
            self.cx.execute('insert into %s (MovieId, movietitle,'
                            'RatingFinal,ROtherFinal, RPictureFinal,'
                            'RDirectorFinal,RStoryFinal,Usercount,'
                            'AttitudeCount, TotalBoxOffice,TodayBoxOffice,'
                            'Rank,ShowDays,isRelease) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)'%(table_name), data)

    def output_end(self):
        if len(self.datas) > 0:
            self.output_db("MTime")
        self.cx.close()

