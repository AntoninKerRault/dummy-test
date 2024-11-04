import matplotlib.pyplot as plt

def all_x_and_y(tile_data, t,instrument,band,measurement_type):
    """
    For any x and y, displays the measurement vs scattering angle graphique.
    
    Parameters: 
    t, intrument, band, measurement_type (all coordinates)
    
    Return: 
    Measurement vs Scattering angle graphique.
    """
    if not (0 <= t < len(tile_data.t) and 
            0 <= instrument < len(tile_data.instrument) and 
            0 <= band < len(tile_data.band) and  
            0 <= measurement_type < len(tile_data.measurement_type)):
        raise IndexError("The indices do not fit with their parameters")

    measurement_xy = tile_data.measurement[t,:,:,instrument,band,measurement_type,:]
    scattering_xy = tile_data.scattering_angle[t,:,:,instrument,band,measurement_type,:]

    plt.figure(figsize=(10, 6))
    plt.scatter(scattering_xy, 
                measurement_xy, 
                label='Measurement x y',
                alpha=0.7)
    plt.xlabel('Scattering Angle (degrees)')
    plt.ylabel('Measurement x y')
    plt.title('Measurement x y vs Scattering Angle')
    plt.show()