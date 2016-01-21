from zorg.driver import Driver


class Motor(Driver):

    def __init__(self, options, connection):
        super(Motor, self).__init__(options, connection)

        self.current_state = False
        self.speed = 0

        self.commands += [
            "turn_on", "turn_off", "is_on", "toggle", "get_speed", "set_speed"
        ]

    def turn_on(self):
        self.current_state = True
        self.connection.digital_write(self.pin, self.speed)

    def turn_off(self):
        self.current_state = False
        self.connection.digital_write(self.pin, 0)

    def toggle(self):
        """
        Toggles the current state of the motor on or off.
        """
        if self.current_state:
            self.turn_off()
        else:
            self.turn_on()

    def is_on(self):
        return self.current_state

    def get_speed(self):
        """
        Return the current speed of the motor.
        """
        return self.speed

    def set_speed(self, value):
        """
        Set the current speed of the motor.
        """
        self.speed = value
