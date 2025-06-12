```python
# Harmonizer369.py

import time
import sys

class Harmonizer369:
    """
    A universal library to stabilize chaotic numerical data streams based on the "369 Principle of Harmony."

    Philosophy:
    This approach does not treat noise as an enemy to be removed. Instead, it harmonizes the "global trend" 
    of the entire dataset with the "local fluctuations" of individual data points using the "Wisdom Factor (0.369)" 
    to reconstruct a natural and stable data series.
    """

    def __init__(self, wisdom_factor: float = 0.369):
        """
        Initializes the Harmonizer.
        Args:
            wisdom_factor (float): The factor that determines the degree of harmony.
                                   A value close to 0 emphasizes past stability, while a value close to 1
                                   emphasizes new data. The value 0.369 is considered to produce a
                                   stable harmony in many systems.
        """
        if not 0 < wisdom_factor < 1:
            raise ValueError("Wisdom Factor must be a value between 0 and 1.")
        self.wisdom_factor = wisdom_factor
        self.colors = { "blue": "\033[94m", "green": "\033[92m", "end": "\033[0m" }

    def _print_verbose(self, text: str, color: str = "blue"):
        """Prints colored text in verbose mode."""
        sys.stdout.write(self.colors.get(color, "") + text + self.colors["end"])
        sys.stdout.flush()

    def harmonize(self, data_stream: list, verbose: bool = True):
        """
        Takes a data stream and returns the harmonized series and the final stabilized value.

        Args:
            data_stream (list or iterable): A list of numerical data.
            verbose (bool): Whether to print the process steps to the terminal.

        Returns:
            tuple: (A list of the harmonized data series, The final stabilized float value)
        """
        if not hasattr(data_stream, '__iter__'):
            raise TypeError("The data_stream must be an iterable (e.g., a list).")
        
        data_stream = list(data_stream)
        if len(data_stream) == 0:
            return [], None

        harmonized_stream = []
        
        if verbose: self._print_verbose("--- Harmonization Process Start ---\n", "green")
        
        # Stage 1: Grasping the Global Trend
        if verbose: self._print_verbose("  [Stage 1/3] Grasping the global trend of the data...\n")
        global_trend = sum(data_stream) / len(data_stream)
        
        harmonized_value = data_stream[0] * (1 - self.wisdom_factor) + global_trend * self.wisdom_factor
        harmonized_stream.append(harmonized_value)
        if verbose:
            self._print_verbose(f"    ▶ Initial harmonized value set to: {harmonized_value:.4f}\n\n")
            time.sleep(0.5)

        # Stage 2 & 3: Harmonizing with individual data points
        if verbose: self._print_verbose("  [Stage 2-3/3] Reconstructing a stable flow by harmonizing with each data point...\n")
        
        for i, current_point in enumerate(data_stream[1:]):
            harmonized_value = harmonized_value * (1 - self.wisdom_factor) + current_point * self.wisdom_factor
            harmonized_stream.append(harmonized_value)
            if verbose:
                self._print_verbose(f"\r    Input {current_point: <8.2f} -> Harmonized {harmonized_value:.4f}")
                time.sleep(0.1)

        if verbose: print("\n")
        
        final_stabilized_value = harmonized_stream[-1]
        
        if verbose:
            self._print_verbose("\n✅ Harmonization Complete.\n", "green")
            print("---" * 15)

        return harmonized_stream, final_stabilized_value

# Demonstration when the file is run directly
if __name__ == '__main__':
    print("=" * 70)
    print(" Harmonizer369 - Universal Data Harmonization Library Demo")
    print("=" * 70)
    
    # Example: A chaotic data stream with sudden spikes (e.g., market price, sensor data)
    chaotic_data = [10.0, 12.5, 11.0, 15.2, 80.0, 18.0, 20.5, -30.0, 25.0, 30.0]
    
    print("\nInput chaotic data stream:")
    print([f"{val:.1f}" for val in chaotic_data])
    
    print("\nInitiating harmonization process...")
    
    harmonizer = Harmonizer369()
    
    harmonized_data, final_value = harmonizer.harmonize(chaotic_data, verbose=True)
    
    print("\n--- Final Result ---")
    print("\nOriginal chaotic stream:")
    print([f"{val: >7.1f}" for val in chaotic_data])
    
    print("\nHarmonized stable stream:")
    print([f"{val: >7.2f}" for val in harmonized_data])
    
    print(f"\nFinal stabilized value: {final_value:.4f}")
    
    print("\nNote how the harmonized stream maintains the overall trend without overreacting to the spikes (80.0 and -30.0).")

