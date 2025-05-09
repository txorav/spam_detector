import 'package:flutter/material.dart';

class Button extends StatelessWidget {
    final String label;
  final VoidCallback? onPressed;

  const Button({
    Key? key,
    required this.label,
    this.onPressed,
  });
  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      decoration: BoxDecoration(
        border: Border.all(
          color: const Color(0xFFE5E7EB), // gray-200
          width: 1,
        ),
        borderRadius: BorderRadius.circular(6),
        color: Colors.white,
      ),
      child: Material(
        color: Colors.transparent,
        child: InkWell(
          onTap: onPressed,
          borderRadius: BorderRadius.circular(6),
          hoverColor: const Color(0xFFF3F4F6), // gray-100
          child: Container(
            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
            child: Center(
              child: Text(
                label,
                style: const TextStyle(
                  fontSize: 14,
                  fontWeight: FontWeight.w500,
                  color: Color(0xFF111827), // gray-900
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }
}