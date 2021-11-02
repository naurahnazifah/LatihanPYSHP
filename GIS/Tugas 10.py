import shapefile
w=shapefile.Writer("./soal10, shapeType=shapefile.POLYGON")
w.shapeType

w.field("kolom1","C")
w.field("kolom2","C")

w.record("ngek","satu")
w.record("ngok","dua")

w.poly([[[5,1], [1,1], [2,3], [6,3], [5,1]]])
w.poly([[[10,1], [6,1], [7,3], [11,3], [10,1]]])

