# mobile_controller
Have you ever wanted to control you Smartphone using your computer? Worry not!! Here are some of the basic tasks that can be executed using your computer on your smartphone.
1) switch on and switch off
2) Call a person
3) Send a what's app message
4) Open a url.
5) >NOTE: If you have a Mi A3 device with passcode unlock you can unlock your phone as well.

# Installation
1) Install the adb tool [link](https://dl.google.com/android/repository/platform-tools-latest-windows.zip)
2) Add the folder path as environment-variable.
3) Run the following command to check if the installation was successful:
```sh
adb version
```

# Requirements
1) Install the package `opencv-python`:
```sh
pip install opencv-python
```
2) Run the python code to see the code running in your terminal!

# How to use?
1) Call a person:
```sh
Example input: 998xxxxxxx
```

2) What's App message:

- [Country Code](https://countrycode.org/) - `Example: IND = +91`
- `Phone` - Enter the 10 digit number
- `Message` - Message you want to send to the user.

3) Open a url:
```sh
Example input: https://google.com/
```
