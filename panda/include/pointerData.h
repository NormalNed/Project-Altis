/**
 * PANDA 3D SOFTWARE
 * Copyright (c) Carnegie Mellon University.  All rights reserved.
 *
 * All use of this software is subject to the terms of the revised BSD
 * license.  You should have received a copy of this license along
 * with this source code in a file named "LICENSE."
 *
 * @file pointerData.h
 * @author drose
 * @date 1999-02-08
 */

#ifndef POINTERDATA_H
#define POINTERDATA_H

#include "pandabase.h"

#include "modifierButtons.h"

BEGIN_PUBLISH
/**
 * Contains the types of pointer device.
 */
enum class PointerType {
  unknown,
  mouse,
  finger,
  stylus,
  eraser,
};
END_PUBLISH

/**
 * Holds the data that might be generated by a 2-d pointer input device, such
 * as the mouse in the GraphicsWindow.
 */
class EXPCL_PANDA_PUTIL PointerData {
PUBLISHED:
  INLINE double get_x() const;
  INLINE double get_y() const;
  INLINE bool get_in_window() const;

public:
  INLINE int get_id() const;
  INLINE PointerType get_type() const;
  INLINE double get_pressure() const;

  void output(std::ostream &out) const;

PUBLISHED:
  MAKE_PROPERTY(x, get_x);
  MAKE_PROPERTY(y, get_y);
  MAKE_PROPERTY(type, get_type);
  MAKE_PROPERTY(id, get_id);
  MAKE_PROPERTY(in_window, get_in_window);
  MAKE_PROPERTY(pressure, get_pressure);

public:
  bool _in_window = false;
  double _xpos = 0.0;
  double _ypos = 0.0;
  double _pressure = 0.0;
  PointerType _type = PointerType::unknown;
  int _id = 0;
};

INLINE std::ostream &operator << (std::ostream &out, const PointerData &md);

#include "pointerData.I"

#endif
