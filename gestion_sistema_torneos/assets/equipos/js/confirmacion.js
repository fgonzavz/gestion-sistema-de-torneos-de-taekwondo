function confirmarEliminacion(id){

    Swal.fire({
        title: 'Estas seguro?',
        text: "NO podrás deshacer esta acción!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, Eliminar!',
        cancelButtonText: 'Cancelar',
      }).then((result) => {
        if (result.value) {

          //redirigir al iusuario a la ruta de eliminar

          window.location.href = "/eliminar_equipo/"+id+"/";

        }

      })
}