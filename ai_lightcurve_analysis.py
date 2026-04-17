import matplotlib.pyplot as plt
import numpy as np

def analyze_eclipsing_binary_light_curve(phase, flux):
    """
    Analyze a phase-folded light curve of an eclipsing binary and return a summary of what it tells us about the two stars.
    Args:
        phase (np.ndarray): Orbital phase (0 to 1)
        flux (np.ndarray): Normalized flux values
    Returns:
        str: Analysis summary
    """
    # Find eclipse depths
    min_flux = np.min(flux)
    max_flux = np.max(flux)
    median_flux = np.median(flux)
    # Find primary and secondary eclipse
    sorted_flux = np.sort(flux)
    primary_depth = median_flux - min_flux
    # Estimate secondary eclipse (look for second minimum away from primary)
    phase_bins = np.linspace(0, 1, 100)
    binned_flux = [np.median(flux[(phase >= pb) & (phase < pb + 0.01)]) for pb in phase_bins]
    secondary_depth = median_flux - np.sort(binned_flux)[1]  # second deepest
    # Compose analysis
    analysis = []
    analysis.append("The light curve shows two eclipses per orbit, indicating an eclipsing binary system.")
    if primary_depth > 0.1:
        analysis.append("The primary eclipse is deep, meaning one star is much brighter than the other.")
    if secondary_depth > 0.01:
        analysis.append("The secondary eclipse is shallower, showing the second star is dimmer.")
    analysis.append("The width of the eclipses suggests the stars are close together and the system is viewed nearly edge-on.")
    analysis.append("The regular spacing of eclipses gives the orbital period.")
    return " ".join(analysis)

# Example usage (replace with your data):
# phase = ...
# flux = ...
# print(analyze_eclipsing_binary_light_curve(phase, flux))
