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
    composer global require "laravel/installer=~1.1"
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
> I have already done this, this structure is already in Git.

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
