import keyboard
import threading

class Drone:
    def __init__(self, x, y):
        self.pos = {"x": x, "y": y}

        self.speed = 0.05

        self.keep = True
        self.returning = False

        # Vector for storing all movements by axises
        self.movements = {"x": 0, "y": 0} 
    
    """
        Starts drone
    """
    def Start(self):
        self.keep = True

        # Creating and running a thread for X-Axis movements
        axisx_thread = threading.Thread(target=self.AxisX)
        axisx_thread.start()

        # Creating and running a thread for Y-Axis movements 
        axisy_thread = threading.Thread(target=self.AxisY)
        axisy_thread.start()
        
        # Creating and running a thread for returning sequence 
        return_thread = threading.Thread(target=self.Return)
        return_thread.start()

    """
        Stops drone
    """
    def Stop(self):
        self.keep = False

    """
        Get keyboard inputs and record movements in X-Axis
    """
    def AxisX(self):
        while self.keep:
            if not self.returning: # If returning sequence is not active
                if keyboard.is_pressed('d'):
                    self.pos["x"] += self.speed
                    self.movements["x"] += self.speed

                if keyboard.is_pressed('a'):
                    self.pos["x"] -= self.speed
                    self.movements["x"] -= self.speed

    """
        Get keyboard inputs and record movements in Y-Axis
    """
    def AxisY(self):
        while self.keep:
            if not self.returning: # If returning sequence is not active
                if keyboard.is_pressed('s'):
                    self.pos["y"] += self.speed
                    self.movements["y"] += self.speed

                if keyboard.is_pressed('w'):
                    self.pos["y"] -= self.speed
                    self.movements["y"] -= self.speed

    """
        Start and stop the returning sequence
    """
    def Return(self):
        while self.keep:
            # Activating and deactivating returning sequence
            if keyboard.is_pressed('r'):
                self.returning = True
            if keyboard.is_pressed('t'):
                self.returning = False

            # Returning sequence
            if self.returning:
                # Stop returning if movements vector is zero
                if -1 < self.movements["x"] < 1 and -1 < self.movements["y"] < 1:
                    self.returning = False
                else:
                    """x_speed = (0 - (self.movements["x"] > 0)) * self.speed
                    y_speed = (0 - (self.movements["y"] > 0)) * self.speed"""

                    if self.movements["x"] > 0:
                        x_speed = -1 * self.speed
                    else:
                        x_speed = +1 * self.speed

                    if self.movements["y"] > 0:
                        y_speed = -1 * self.speed
                    else:
                        y_speed = +1 * self.speed

                    self.pos["x"] += x_speed
                    self.movements["x"] += x_speed

                    self.pos["y"] += y_speed
                    self.movements["y"] += y_speed

