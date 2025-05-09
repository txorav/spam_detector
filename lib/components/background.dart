import 'package:flutter/material.dart';

class Circles extends StatefulWidget {
  const Circles({super.key});

  @override
  State<Circles> createState() => _CirclesState();
}

class _CirclesState extends State<Circles> {
  Color color = Color(0x0A000000);
  @override
  Widget build(BuildContext context) {
    return MouseRegion(
      onExit: (_) async {
        await Future.delayed(Duration(milliseconds: 10), () {
          setState(() {
            color = Color(0x0A000000);
          });
        });
      },
      onHover: (event) async {
        setState(() {
          color = Color.fromARGB(
            (255 / event.position.dx + event.position.dy - event.distance)
                    .toInt() +
                200,
            59,
            130,
            246,
          );
        });
      },
      child: Container(
        width: 5,
        height: 5,
        child: null,
        margin: const EdgeInsets.all(5),
        decoration: BoxDecoration(shape: BoxShape.circle, color: color),
      ),
    );
  }
}
