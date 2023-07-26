create table Contact(
  id                   SERIAL PRIMARY KEY,
  phoneNumber          VARCHAR(15),
  email                VARCHAR(100),
  linkedId             integer,
  linkPrecedence       VARCHAR(15),
  createdAt            timestamp default current_timestamp not null,
  updatedAt            timestamp not null,
  deletedAt            timestamp
);

insert into contact(phonenumber,email,linkedid,linkprecedence,updatedat,deletedat)
values('123','email',234,'fxhxh','2016-06-22 19:10:25-07',NULL);