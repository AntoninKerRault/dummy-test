from utils.tools import scattering_angle
import pytest
import numpy as np

@pytest.mark.parametrize("sza, vza, raa, expected", [
    (0, 0, 0, 180),  
    (90, 90, 0, 180),  
    (45, 45, 180, 90),
    (60, 30, 90, 115.658906),
])
def test_scattering_angle_valid(sza, vza, raa, expected):
    """Test with valid angles."""
    result = scattering_angle(sza, vza, raa)
    np.testing.assert_almost_equal(result, expected, decimal=6)  # Tolérance de 6 décimales

@pytest.mark.parametrize("sza, vza, raa, expected", [
    (-10, 30, 90, 148.525051),   
    (60, -20, 90, 118.024320),    
    (60, 30, -50, 135.344690),    
    (95, 30, 90, 85.671249),     
    (60, 100, 90, 85.019074),    
    (60, 30, 370, 149.254545),    
])
def test_scattering_angle_valid_negatif(sza, vza, raa, expected):
    """Test with valid angles."""
    result = scattering_angle(sza, vza, raa)
    np.testing.assert_almost_equal(result, expected, decimal=6)

@pytest.mark.parametrize("sza, vza, raa", [
    (0, 0, 0),       
    (90, 90, 360),   
])
def test_scattering_angle_boundaries(sza, vza, raa):
    """Test with boundary values for angles."""
    try:
        scattering_angle(sza, vza, raa)
    except ValueError:
        pytest.fail(f"scattering_angle raised ValueError unexpectedly for sza={sza}, vza={vza}, raa={raa}")
        