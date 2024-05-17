# Raspberry Pi Setup

User: ti3groep
Password: N02A5

## phpmyadmin

MySQL application password: 

GRANT ALL PRIVILEGES ON *.* TO 'ti3groep'@'localhost' IDENTIFIED BY 'BG32L2D' WITH GRANT OPTION;

username: ti3groep
password: BG32L2D

## MariaDB

Root password: Z54O541

## Raspi Read/Write toestemming voorbeeld

```
Its is simple.

On normal situation, http daemon run as some user and group, www-data on debian (raspbian).
Standard html files are stored on /var/www/, owned by root:root, with permissive permission, all can read, but only root can write.
To ordinary user write to /var/www need to takeover it. Supposed the use is pi.
sudo chown -R pi:www-data /var/www
Also, need to set user and group permission:
sudo chmod u+rxw,g+rx-w,o-rwx /var/www

Now, /var/www can be read,write and chdir by user pi, group www-data can chdir and read. Other not have access.

---

sudo chmod g+s /var/www
Any new file created on /var/www belong to group www-data.
If have files on /var/www, change user and group, and allow to group www-data read.
For file chmod u+rw,g+r-xw,o-rwx
For directory chmod u+rwx,g+rx-w,o-rxw
Now, user pi can manipulate files on /var/www and httpd can read, but not write.
```