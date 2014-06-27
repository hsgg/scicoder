CREATE TABLE "student" ("id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE , "first_name" TEXT, "last_name" TEXT, "city_id" INTEGER, "status_id" INTEGER);
CREATE TABLE "supervisor" ("id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE , "first_name" TEXT, "last_name" TEXT, "room_number" TEXT);
CREATE TABLE "student_to_supervisor" ("student_id" INTEGER NOT NULL , "supervisor_id" INTEGER NOT NULL , PRIMARY KEY ("student_id", "supervisor_id"));
CREATE TABLE "city" ("id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE , "label" TEXT);
CREATE TABLE "club" ("id" INTEGER PRIMARY KEY  NOT NULL ,"label" TEXT DEFAULT (null) );
CREATE TABLE "status" ("id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE , "label" TEXT check(typeof("label") = 'text') );
CREATE TABLE "student_to_club" ("student_id" INTEGER NOT NULL , "club_id" INTEGER NOT NULL , PRIMARY KEY ("student_id", "club_id"));
