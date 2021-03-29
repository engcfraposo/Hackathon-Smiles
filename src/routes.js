
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createDrawerNavigator } from '@react-navigation/drawer';
import { createStackNavigator } from '@react-navigation/stack';

import Presentation from './pages/presentation';
import StartingSearch from './pages/startingSearch';
import Quiz from './pages/quiz';
import Home from './pages/home';
import Packs from './pages/packs';


const Drawer = createDrawerNavigator();
const Stack = createStackNavigator();


const Screen1 = () => {
    return(
            
        <Drawer.Navigator initialRouteName="Home">
            <Drawer.Screen name="Home" component={Home} />
            <Drawer.Screen name="Presentation" component={Presentation} />
            <Stack.Screen name="StartingSearch" component={StartingSearch} />
            <Stack.Screen name="Quiz" component={Quiz} />
            <Stack.Screen name="Packs" component={Packs} />
        </Drawer.Navigator>
    )
    
}


const Routes = () =>{
    return (

        <NavigationContainer independent={true}>
        
        <Stack.Navigator
                initialRouteName="Home"
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


