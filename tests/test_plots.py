import xarray as xr
from utils.plot import all_x_and_y

tile_data = xr.open_dataset('tile_polder.nc')
sza = tile_data['solar_zenith_angle']
vza = tile_data['viewing_zenith_angle']
raa = tile_data['relative_azimuth_angle']
scattering_angle_value = scattering_angle(sza, vza, raa)
tile_data['scattering_angle'] = scattering_angle_value

import pytest

@pytest.mark.parametrize("t, instrument, band, measurement_type", [
    (5, 0, 3, 1),  
    (0, 0, 0, 0),  
    (29, 0, 5, 2), 
])
def test_valid_indices(t, instrument, band, measurement_type):
    """Test with valid indices."""
    try:
        all_x_and_y(t, instrument, band, measurement_type)
    except IndexError:
        pytest.fail(f"all_x_and_y raised IndexError unexpectedly for t={t}, instrument={instrument}, band={band}, measurement_type={measurement_type}!")

@pytest.mark.parametrize("t, instrument, band, measurement_type", [
    (30, 0, 3, 1),  
    (5, 1, 3, 1),   
    (5, 0, 6, 1),   
    (5, 0, 3, 3),  
])
def test_invalid_indices(t, instrument, band, measurement_type):
    """Test with invalid indices."""
    with pytest.raises(IndexError):
        all_x_and_y(t, instrument, band, measurement_type)

@pytest.mark.parametrize("t, instrument, band, measurement_type", [
    (0, 0, 0, 0),    
    (29, 0, 5, 2),   
])
def test_boundary_indices(t, instrument, band, measurement_type):
    """Test with boundary indices."""
    try:
        all_x_and_y(t, instrument, band, measurement_type)
    except IndexError:
        pytest.fail(f"all_x_and_y raised IndexError unexpectedly for t={t}, instrument={instrument}, band={band}, measurement_type={measurement_type}!")