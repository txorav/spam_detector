import 'package:flutter/material.dart';

class Box extends StatelessWidget {
  final List<Widget> children;

  Box({required this.children});

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        border: Border.all(
          color: const Color(0xFFE5E7EB), // gray-200
          width: 1,
        ),
        borderRadius: BorderRadius.circular(6),
        color: Colors.white,
        boxShadow: const [
          BoxShadow(
            color: Color(0x08000000), // rgba(0,0,0,0.03)
            blurRadius: 2,
            offset: Offset(0, 1),
          ),
        ],
      ),
      child: Material(
        color: Colors.transparent,
        child: Container(
          padding: const EdgeInsets.all(16),
          child: Column(
            children: children,
          ),
        ),
      ),
    );
  }
}
