import numpy as np

def scattering_angle(sza, vza, raa):
    """
    Calculates the scattering angle from the solar zenith angle (sza), the viewing zenith    angle (vza) and the relative azimuth angle (raa).
    
    Parameters: 
    sza (numpy.ndarray): Solar zenith angle in degrees.
    vza (numpy.ndarray): Zenith viewing angle in degrees.
    raa (numpy.ndarray): Relative azimuth angle in degrees.
    
    Return: 
    Diffusion angle in degrees.
    """
    sza_rad = np.radians(sza)
    vza_rad = np.radians(vza)
    raa_rad = np.radians(raa)
    
    cos_theta = -np.cos(sza_rad) * np.cos(vza_rad) - np.sin(sza_rad) * np.sin(vza_rad) * np.cos(raa_rad)
    
    theta = np.degrees(np.arccos(cos_theta))
    
    return theta
