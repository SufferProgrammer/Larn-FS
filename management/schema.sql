drop table if exists user;
    create table users (
    id integer primary key autoincrement,
    user text not null,
    pass text not null
);
