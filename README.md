# ros2-turtle-circle

A ROS 2 Humble project that controls the `turtlesim` simulator by publishing velocity commands to make the turtle draw a circle and stop automatically.

**ROS Version:** Humble

## Concepts Used

- Python
- `rclpy`
- Topics
- Publishers
- Timers
- `geometry_msgs/msg/Twist`

## System Design

| **Circle Controller Node** | **Topic** | **Turtlesim Node** |
| -------------------------- | --------- | ------------------ |
| Creates a Publisher | `/turtle1/cmd_vel` | Creates a Subscription |
| Publishes `Twist` messages | → | Receives velocity commands |
| `timer_callback()` | → | Moves the turtle |
| Counter-based stopping logic | → | Stops after receiving zero velocity |

## How It Works

The publisher node periodically sends `Twist` messages to the `/turtle1/cmd_vel` topic using a timer callback. A callback counter is used to determine when to stop publishing movement commands. Once the callback limit is reached, a final `Twist` message with zero linear and angular velocity is published, stopping the turtle.

> **Note:** Since the stopping logic is based on a timer callback counter rather than the turtle's actual position, the circle may not be perfectly accurate. A future improvement would be to subscribe to `/turtle1/pose` and use pose feedback for more precise motion control.

## Demo

A demo video and the terminal commands used to run the project are included in this repository.
