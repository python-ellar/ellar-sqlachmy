from ellar.common import Module, exception_handler, IExecutionContext, JSONResponse, Response
from ellar.core import ModuleBase, LazyModuleImport as lazyLoad
from ellar.samples.modules import HomeModule


@Module(modules=[HomeModule,  lazyLoad('db.module:DbModule')])
class ApplicationModule(ModuleBase):
    @exception_handler(404)
    def exception_404_handler(cls, ctx: IExecutionContext, exc: Exception) -> Response:
        return JSONResponse(dict(detail="Resource not found."), status_code=404)