import 'dart:io';

import 'package:flutter/material.dart';
import 'package:pattern_box/pattern_box.dart';
import 'package:simple_ui_library/components/background.dart';
import 'package:simple_ui_library/components/box.dart';
import 'package:simple_ui_library/components/button.dart';
import 'package:simple_ui_library/components/textfield.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Flutter Demo',
      theme: ThemeData(
        // This is the theme of your application.
        //
        // TRY THIS: Try running your application with "flutter run". You'll see
        // the application has a purple toolbar. Then, without quitting the app,
        // try changing the seedColor in the colorScheme below to Colors.green
        // and then invoke "hot reload" (save your changes or press the "hot
        // reload" button in a Flutter-supported IDE, or press "r" if you used
        // the command line to start the app).
        //
        // Notice that the counter didn't reset back to zero; the application
        // state is not lost during the reload. To reset the state, use hot
        // restart instead.
        //
        // This works for code too, not just values: Most code changes can be
        // tested with just a hot reload.
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
      ),
      home: Test(),
    );
  }
}

List<Widget> createCircles() {
  List<Widget> circles = [];
  for (int i = 0; i < 500 / 17.toInt(); i++) {
    circles.add(Circles());
  }
  return circles;
}

class Test extends StatefulWidget {
  const Test({super.key});

  @override
  State<Test> createState() => _TestState();
}

TextEditingController thing = TextEditingController();
TextEditingController thingie = TextEditingController();
bool isho = false;
bool isSpam = false;
bool isFirst = true;
bool isLoading = false;

class _TestState extends State<Test> {
  Future<ProcessResult> runPythonScript(String text) async {
    ProcessResult res = await Process.run('python', [
      r'C:\Users\DEV\Documents\projects\SpamDetection\spam_detector\backend\main.py',
      text,
    ]);
    return res;
  }

  void checkEmail(String text,String modelName) async {
    setState(() {
      isLoading = true;
    });
    ProcessResult result = await Process.run('python3', [
      r'C:\Users\DEV\Documents\projects\SpamDetection\spam_detector\backend\main.py',
      text,
      modelName,
    ]);
    print(result.stdout);
    print(result.stderr);
    setState(() {
      isLoading = false;
      
      int.parse(result.stdout) == 0 ? isSpam = false : isSpam = true;
    });
    print(isSpam);
  }
  @override
  void initState() {
    // TODO: implement initState
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      body: Center(
        child: Stack(
          clipBehavior: Clip.hardEdge,
          children: [
            PatternBoxWidget(
              pattern: DottedWavePainter(color: Color(0x0A000000)),
            ),
            Center(
              child: Container(
                constraints: BoxConstraints(maxWidth: 500, maxHeight: 500),
                clipBehavior: Clip.hardEdge,
                width: 500,
                height: 500,
                padding: const EdgeInsets.all(25),
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Text(
                      'Spam Detector',
                      style: TextStyle(
                        color: Colors.black87,
                        fontWeight: FontWeight.bold,
                        fontSize: 40,
                      ),
                    ),
                    TextField(
                      controller: thing,
                      decoration: InputDecoration(
                        hintText: "Please write an email to know whether its spam or no",
                        focusedBorder: OutlineInputBorder(
                          borderSide: BorderSide(
                            width: 2,
                            color: Colors.black87,
                          ),
                        ),
                        focusColor: Colors.black87,
                        hoverColor: Colors.black87,
                        border: OutlineInputBorder(
                          borderSide: BorderSide(
                            width: 2,
                            color: Color(0x4C4B5563),
                          ),
                        ),
                      ),
                    ),
                    TextField(
                      controller: thingie,
                      decoration: InputDecoration(
                        hintText: "please write nb for naivebayes and dt for decision tree classifier and lr for logistic regression",
                        focusedBorder: OutlineInputBorder(
                          borderSide: BorderSide(
                            width: 2,
                            color: Colors.black87,
                          ),
                        ),
                        focusColor: Colors.black87,
                        hoverColor: Colors.black87,
                        border: OutlineInputBorder(
                          borderSide: BorderSide(
                            width: 2,
                            color: Color(0x4C4B5563),
                          ),
                        ),
                      ),
                    ),
                    MouseRegion(
                      onExit: (_) {
                        setState(() {
                          isho = false;
                        });
                      },
                      onEnter: (_) {
                        setState(() {
                          isho = true;
                        });
                      },
                      child: GestureDetector(
                        onTap: isLoading ? null : () => checkEmail(thing.text,thingie.text),
                        child: Container(
                          width: 400,
                          child: Center(
                            child:
                                isLoading
                                    ? CircularProgressIndicator(strokeWidth: 2)
                                    : Text('Check'),
                          ),
                          height: 50,
                          decoration: BoxDecoration(
                            color: Colors.white,
                            borderRadius: BorderRadius.circular(5),
                            border: Border.all(
                              color: isho ? Colors.black87 : Color(0x0A000000),
                            ),
                          ),
                        ),
                      ),
                    ),
                    Container(
                      width: 300,
                      child:
                          isSpam
                              ? Center(
                                child: Text(
                                  "Spam",
                                  style: TextStyle(color: Color(0xFFB71C1C)),
                                ),
                              )
                              : Center(
                                child: Text(
                                  "Natural",
                                  style: TextStyle(color: Color(0xFF388E3C)),
                                ),
                              ),
                      height: 50,
                      decoration: BoxDecoration(
                        color: Colors.white,
                        borderRadius: BorderRadius.circular(5),
                        boxShadow: [
                          BoxShadow(
                            color: Color(0x0A000000),
                            blurRadius: 12,
                            offset: Offset(0, 2),
                          ),
                        ],
                        border: Border.all(
                          color:
                              isFirst
                                  ? Color(0x4C4B5563)
                                  : isSpam
                                  ? Color(0xFFB71C1C)
                                  : Color(0xFF388E3C),
                        ),
                      ),
                    ),
                  ],
                ),
                decoration: BoxDecoration(
                  color: Colors.white,
                  borderRadius: BorderRadius.circular(5),
                  boxShadow: [
                    BoxShadow(
                      color: Color(0x0A000000),
                      blurRadius: 12,
                      offset: Offset(0, 2),
                    ),
                  ],
                  border: Border.all(color: Color(0x4C4B5563)),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
