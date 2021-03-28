
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createDrawerNavigator } from '@react-navigation/drawer';
import { createStackNavigator } from '@react-navigation/stack';

import Presentation from './pages/presentation';
import StartingSearch from './pages/startingSearch';
import Home from './pages/home'
// import Register from './pages/register';
// import Points from './pages/points';
// import Detail from './pages/detail';
// import ReadyToGo from './pages/ready';
// import Maps from './pages/map';
// import Cupons from './pages/cupons';

const Drawer = createDrawerNavigator();
const Stack = createStackNavigator();


const Screen1 = () => {
    return(
            
        <Drawer.Navigator initialRouteName="Home">
    
        <Drawer.Screen name="Home" component={Home} />
        <Drawer.Screen name="Presentation" component={Presentation} />
        <Stack.Screen name="StartingSearch" component={StartingSearch} />
        
        </Drawer.Navigator>
    )
    
}


const Routes = () =>{
    return (

        <NavigationContainer independent={true}>
        
        <Stack.Navigator
                initialRouteName="StartingSearch"
                headerMode="none"
                screenOptions={{
                    cardStyle:{
                        backgroundColor:'#f0f0f5'
                    }
                }}
             >           
           
           <Stack.Screen name="Drawer" component={Screen1} />
        </Stack.Navigator>
        </NavigationContainer>
    )
}

export default Routes;


