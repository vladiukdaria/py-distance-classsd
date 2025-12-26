class Distance:
    # Initialize with distance in meters by default
    def __init__(self, meters=0.0):
        self.meters = float(meters)
    
    # Class method to create Distance from kilometers
    @classmethod
    def from_kilometers(cls, km):
        return cls(km * 1000)
    
    # Class method to create Distance from miles
    @classmethod
    def from_miles(cls, miles):
        return cls(miles * 1609.34)
    
    # Represent the object as a string
    def __str__(self):
        return f"{self.meters:.2f} meters"
    
    # Adding two Distance objects
    def __add__(self, other):
        if isinstance(other, Distance):
            return Distance(self.meters + other.meters)
        raise TypeError("Can only add Distance to Distance")
    
    # Subtracting two Distance objects
    def __sub__(self, other):
        if isinstance(other, Distance):
            return Distance(self.meters - other.meters)
        raise TypeError("Can only subtract Distance from Distance")
    
    # Convert to kilometers
    def to_kilometers(self):
        return self.meters / 1000
    
    # Convert to miles
    def to_miles(self):
        return self.meters / 1609.34

# Example usage
if __name__ == "__main__":
    d1 = Distance(500)  # 500 meters
    d2 = Distance.from_kilometers(2)  # 2 kilometers
    d3 = Distance.from_miles(1)  # 1 mile

    print(f"d1: {d1}")  # d1: 500.00 meters
    print(f"d2: {d2}")  # d2: 2000.00 meters
    print(f"d3: {d3}")  # d3: 1609.34 meters

    # Arithmetic operations
    total_distance = d1 + d2 + d3
    print(f"Total Distance: {total_distance}")  # Total in meters

    # Conversions
    print(f"Total in kilometers: {total_distance.to_kilometers():.2f} km")
    print(f"Total in miles: {total_distance.to_miles():.2f} miles")
    def __ge__(self, other: Union[Distance, int, float]) -> bool:
        return self.km >= (other.km if isinstance(other, Distance) else other)
