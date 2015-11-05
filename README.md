# Siren
© Erik to the L, Stijn to the H

# Composer

1. install curl
    ```shell
    sudo apt-get install curl
    ```

2. download composer.phar
    ```shell
    curl -sS https://getcomposer.org/installer | php
    ```

3. move composer.phar to local binaries folder so we can execute the command
    ```shell
    sudo mv composer.phar /usr/local/bin
    ```
(test: composer.phar in any folder, command must be found)


# Install Laravel via Composer

1. download laravel installer
    ```shell
    composer global require "laravel/installer=~1.1.3"
    ```

2. add laravel command to PATH
we need to do this so we can execute the laravel command from any place on our system
a good place to this is in the .bashrc file:
    ```shell
    sudo nano .bashrc
    ```
go to the end of the file and add:
    ```shell
    export PATH="~/.composer/vendor/bin:$PATH"
    ```
exit the terminal and start a new one to reload the PATH
(test: laravel in any folder, command must be found)

# Create a new project with Laravel
> This does not need to happen when you clone this project from Github.
It has already been done for you ;-)

1. Go to the main Siren folder
    ```shell
    cd Siren
    ```
2. Start the new project
    ```
    laravel new siren
    ```

3. Our directory structure is now:
    ```
    Siren
    |    README.md
    |----Siren
         |---- app
         |---- bootstrap
         |---- package.json
         |---- ....
    ```

### Check the security settings
The webserver will need to write to your storage folder.
So check that this folder has the correct access rights.
```shell
sudo chmod 775 storage
```

### Create the secret key
Copy or move the orginal env example file to a real .env file
This file is located in the root of the Laravel app we created
```shell
 cp .env.example .env
```
.env will be ignored by git as it is set in gitignore.
So adding your own secret in this file will not be visible on github.com
Now let's generate the key that will be put in this file.
```shell
php artisan key:generate
```
# Set up a virtual host for our local website (Apache)
It can't be better explained than on the following site:
https://www.digitalocean.com/community/tutorials/how-to-set-up-apache-virtual-hosts-on-ubuntu-14-04-lts

When configuring the host, make sure the document root points to the public directory of our Laravel app.
So something like should do it:
```shell
<VirtualHost 127.0.0.2:80>
	ServerAdmin admin@siren.com
	ServerName siren.com
	ServerAlias www.siren.com
	DocumentRoot /home/stijn/Development/Siren/siren/public
	ErrorLog ${APACHE_LOG_DIR}/error.log
	CustomLog ${APACHE_LOG_DIR}/access.log combined
	<Directory />
      Require all granted
    </Directory>
</VirtualHost>
```
reload and restart the apache service and your local Siren site should be up and running.
As you see in my configuration above, I have to browse to 127.0.0.2 and there it is, siren.com on your local machine!

# Add Twitter Bootstrap to our project
## Install required packages
```shell
cd siren
composer.phar update
npm install # probably with sudo
```

> this adds two packages to our application: laravel-elixr and bootstrap-sass

## Modify app.scss
In the directory /resources/assets/sass modify the app.scss file.
Uncomment the first line so the file looks something like:
```scss
@import "node_modules/bootstrap-sass/assets/stylesheets/bootstrap";
```

## Modify gulpfile.js for extra bootstrap requirements
In the main directory open gulpfile.js and replace following piece of code:
```javascript
elixir(function(mix) {
  mix.sass('app.scss');
});
```
by this:
```javascript
elixir(function(mix) {
    var bootstrapPath = 'node_modules/bootstrap-sass/assets';
    mix.sass('app.scss')
        .copy(bootstrapPath + '/fonts', 'public/fonts')
        .copy(bootstrapPath + '/javascripts/bootstrap.min.js', 'public/js');
});
```

## Run gulp to get the bootstrap source files
```shell
gulp
```
When the gulp command is not found, install it via Node Package Manager
```shell
sudo npm install -g gulp
```
Now have a look at the public folder, all the CSS, fonts and JS should be there!
