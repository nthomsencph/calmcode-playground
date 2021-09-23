
# cookiecutter commands
Automated project templates!

Code-along @ https://calmcode.io/cookiecutter/the-problem.html <br>

## Install cookiecutter
`pip install cookiecutter`

## Create required components
    touch cookiecutter.json
And add 
    
    {
       "project" : "project",
       "author"  : "author"
    } 
Then create folder 
`{{cookiecutter.project}}`
and create `readme.md` inside with text

    readme of {{cookiecutter.project}}

    This package was made by {{cookiecutter.author}} as part of a calmcode.io code-along!



## Run cookiecutter
    cookiecutter .
 It will prompt you to enter a name for the project you want to create. Note that you can leave the fields blank. they wil default to the value in brackets, i.e. the values specified in `cookiecutter.json`.

    project [project]: hello-world
    author [author]: your-name


## See results
The above commands generate an automated, customized readme file. We can add any kind of file this way. See the other files. 

## Cookiecut via git
    cookiecutter git@gitlab.com:<user>/<repo>.git


