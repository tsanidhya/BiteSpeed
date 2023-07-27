create table if not exists Contact(
  id                   SERIAL PRIMARY KEY,
  phoneNumber          VARCHAR(15),
  email                VARCHAR(100),
  linkedId             integer,
  linkPrecedence       VARCHAR(15),
  createdAt            timestamp default current_timestamp not null,
  updatedAt            timestamp not null,
  deletedAt            timestamp
);

--insert into contact(phonenumber,email,linkedid,linkprecedence,updatedat,deletedat)
-- values('1234','dummy@a.com',NULL,'primary','2023-07-24 20:12:08Z',NULL);